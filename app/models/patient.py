"""Patient model - Core transactional data"""
from sqlalchemy import Column, Integer, String, Date, Enum as SQLEnum, DateTime
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base


class Gender(str, enum.Enum):
    """Gender enum"""
    MALE = "M"
    FEMALE = "F"
    OTHER = "O"


class Patient(Base):
    """Patient model representing a person in the health system"""
    __tablename__ = "patients"

    id = Column(Integer, primary_key=True, index=True)

    # Basic demographics
    first_name = Column(String(100), nullable=False)
    last_name = Column(String(100), nullable=False)
    email = Column(String(255), unique=True, index=True)
    phone = Column(String(20))

    # Personal info
    date_of_birth = Column(Date, nullable=False)
    gender = Column(SQLEnum(Gender), nullable=False)
    city = Column(String(100))

    # Metadata
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    digital_twin = relationship("DigitalTwin", back_populates="patient", uselist=False)
    chat_sessions = relationship("ChatSession", back_populates="patient")
    health_goals = relationship("HealthGoal", back_populates="patient")

    def __repr__(self):
        return f"<Patient {self.first_name} {self.last_name}>"
