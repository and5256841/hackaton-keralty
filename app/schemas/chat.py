"""Pydantic schemas for chat endpoints"""
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ChatMessageRequest(BaseModel):
    """Request to send a message in chat"""
    session_id: int
    message: str


class ChatMessageResponse(BaseModel):
    """Response from the chat"""
    session_id: int
    user_message: str
    assistant_message: str
    timestamp: datetime

    class Config:
        from_attributes = True


class ChatSessionCreate(BaseModel):
    """Create a new chat session"""
    patient_id: int
    program_focus: Optional[str] = None


class ChatSessionResponse(BaseModel):
    """Chat session info"""
    id: int
    patient_id: int
    started_at: datetime
    is_active: bool
    program_focus: Optional[str] = None

    class Config:
        from_attributes = True
