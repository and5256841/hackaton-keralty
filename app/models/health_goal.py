"""Health Goals model - Patient's health objectives and progress"""
from sqlalchemy import Column, Integer, String, Text, Float, ForeignKey, DateTime, Boolean, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base


class GoalStatus(str, enum.Enum):
    """Status of a health goal"""
    NOT_STARTED = "not_started"
    IN_PROGRESS = "in_progress"
    COMPLETED = "completed"
    ABANDONED = "abandoned"


class HealthGoal(Base):
    """
    Health goals for patients - shown in their dashboard
    These are personalized objectives based on their digital twin
    """
    __tablename__ = "health_goals"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), nullable=False)

    # Goal details
    title = Column(String(200), nullable=False)
    description = Column(Text)
    target_value = Column(String(100))  # e.g., "140/90 mmHg", "25 BMI"
    current_value = Column(String(100))  # Current measurement

    # Progress tracking
    status = Column(SQLEnum(GoalStatus), default=GoalStatus.NOT_STARTED)
    progress_percentage = Column(Float, default=0.0)  # 0.0 to 100.0

    # Related program
    program_code = Column(String(50))  # Links to which program this goal belongs to

    # Dates
    created_at = Column(DateTime, default=datetime.utcnow)
    target_date = Column(DateTime, nullable=True)
    completed_at = Column(DateTime, nullable=True)

    # Relationship
    patient = relationship("Patient", back_populates="health_goals")

    def __repr__(self):
        return f"<HealthGoal patient_id={self.patient_id} title={self.title}>"
