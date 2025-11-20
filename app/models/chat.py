"""Chat models for 'Yo del Futuro' conversations"""
from sqlalchemy import Column, Integer, String, Text, ForeignKey, DateTime, Boolean
from sqlalchemy.orm import relationship
from datetime import datetime
from app.database import Base


class ChatSession(Base):
    """Chat session between patient and their 'future self'"""
    __tablename__ = "chat_sessions"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)

    # Session metadata
    started_at = Column(DateTime, default=datetime.utcnow)
    ended_at = Column(DateTime, nullable=True)
    is_active = Column(Boolean, default=True)

    # Context for this session
    program_focus = Column(String(100))  # Which program is being discussed

    # Relationships
    patient = relationship("Patient", back_populates="chat_sessions")
    messages = relationship("ChatMessage", back_populates="session", order_by="ChatMessage.timestamp")

    def __repr__(self):
        return f"<ChatSession patient_id={self.patient_id} active={self.is_active}>"


class ChatMessage(Base):
    """Individual messages in a chat session"""
    __tablename__ = "chat_messages"

    id = Column(Integer, primary_key=True, index=True)
    session_id = Column(Integer, ForeignKey("chat_sessions.id"), nullable=False)

    # Message content
    role = Column(String(20), nullable=False)  # "user" or "assistant" (future self)
    content = Column(Text, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)

    # Relationship
    session = relationship("ChatSession", back_populates="messages")

    def __repr__(self):
        return f"<ChatMessage session_id={self.session_id} role={self.role}>"
