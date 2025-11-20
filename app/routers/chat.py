"""Chat endpoints - 'Yo del Futuro' conversation"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, date
from typing import List

from app.database import get_db
from app.models.chat import ChatSession, ChatMessage
from app.models.patient import Patient
from app.models.digital_twin import DigitalTwin
from app.schemas.chat import (
    ChatSessionCreate,
    ChatSessionResponse,
    ChatMessageRequest,
    ChatMessageResponse
)
from app.services.openai_service import openai_service

router = APIRouter(prefix="/chat", tags=["Chat"])


@router.post("/session", response_model=ChatSessionResponse)
def create_chat_session(
    session_data: ChatSessionCreate,
    db: Session = Depends(get_db)
):
    """Create a new chat session for a patient"""

    # Verify patient exists
    patient = db.query(Patient).filter(Patient.id == session_data.patient_id).first()
    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    # Create session
    session = ChatSession(
        patient_id=session_data.patient_id,
        program_focus=session_data.program_focus,
        is_active=True
    )

    db.add(session)
    db.commit()
    db.refresh(session)

    return session


@router.post("/message", response_model=ChatMessageResponse)
def send_chat_message(
    message_data: ChatMessageRequest,
    db: Session = Depends(get_db)
):
    """Send a message in the chat and get response from 'yo del futuro'"""

    if not openai_service:
        raise HTTPException(
            status_code=503,
            detail="OpenAI service not configured. Please set OPENAI_API_KEY"
        )

    # Get session
    session = db.query(ChatSession).filter(ChatSession.id == message_data.session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Chat session not found")

    # Get patient and digital twin
    patient = db.query(Patient).filter(Patient.id == session.patient_id).first()
    digital_twin = db.query(DigitalTwin).filter(DigitalTwin.patient_id == patient.id).first()

    if not digital_twin:
        raise HTTPException(status_code=404, detail="Digital twin not found for patient")

    # Calculate age
    today = date.today()
    age = today.year - patient.date_of_birth.year
    if today.month < patient.date_of_birth.month or \
       (today.month == patient.date_of_birth.month and today.day < patient.date_of_birth.day):
        age -= 1

    # Build patient context for OpenAI
    patient_context = {
        "name": patient.first_name,
        "age": age,
        "conditions": digital_twin.conditions,
        "risk_level": digital_twin.risk_level.value,
        "complication_probability_90d": digital_twin.complication_probability_90d,
        "recommended_programs": digital_twin.recommended_programs
    }

    # Get conversation history
    previous_messages = db.query(ChatMessage).filter(
        ChatMessage.session_id == session.id
    ).order_by(ChatMessage.timestamp).all()

    conversation_history = [
        {"role": msg.role, "content": msg.content}
        for msg in previous_messages
    ]

    # Save user message
    user_msg = ChatMessage(
        session_id=session.id,
        role="user",
        content=message_data.message
    )
    db.add(user_msg)

    # Get AI response
    try:
        ai_response = openai_service.chat_as_future_self(
            patient_context=patient_context,
            conversation_history=conversation_history,
            user_message=message_data.message
        )
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=str(e))

    # Save assistant message
    assistant_msg = ChatMessage(
        session_id=session.id,
        role="assistant",
        content=ai_response
    )
    db.add(assistant_msg)

    db.commit()

    return ChatMessageResponse(
        session_id=session.id,
        user_message=message_data.message,
        assistant_message=ai_response,
        timestamp=datetime.utcnow()
    )


@router.get("/session/{session_id}/history")
def get_chat_history(
    session_id: int,
    db: Session = Depends(get_db)
):
    """Get all messages in a chat session"""

    session = db.query(ChatSession).filter(ChatSession.id == session_id).first()
    if not session:
        raise HTTPException(status_code=404, detail="Session not found")

    messages = db.query(ChatMessage).filter(
        ChatMessage.session_id == session_id
    ).order_by(ChatMessage.timestamp).all()

    return {
        "session_id": session_id,
        "messages": [
            {
                "role": msg.role,
                "content": msg.content,
                "timestamp": msg.timestamp
            }
            for msg in messages
        ]
    }
