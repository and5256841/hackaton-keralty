"""Digital Twin model - Individual patient's digital representation"""
from sqlalchemy import Column, Integer, String, Float, JSON, ForeignKey, DateTime, Enum as SQLEnum
from sqlalchemy.orm import relationship
from datetime import datetime
import enum
from app.database import Base


class RiskLevel(str, enum.Enum):
    """Risk level classification"""
    HEALTHY = "healthy"
    SUSCEPTIBLE = "susceptible"
    STABLE_CONDITION = "stable_condition"
    HIGH_COMPLEXITY = "high_complexity"


class DigitalTwin(Base):
    """
    Digital Twin - Individual representation of patient's health state
    This is the core of personalization
    """
    __tablename__ = "digital_twins"

    id = Column(Integer, primary_key=True, index=True)
    patient_id = Column(Integer, ForeignKey("patients.id"), unique=True, nullable=False)

    # Clinical risk assessment
    risk_level = Column(SQLEnum(RiskLevel), default=RiskLevel.HEALTHY)
    complication_probability_90d = Column(Float, default=0.0)  # Probability of complication in 90 days
    estimated_cost_90d = Column(Float, default=0.0)  # Estimated cost if no intervention

    # Health conditions (JSON array of condition names)
    conditions = Column(JSON, default=list)  # e.g., ["hypertension", "obesity"]

    # Pending controls
    pending_controls = Column(JSON, default=list)  # e.g., ["blood_pressure", "glucose"]

    # Usage patterns
    emergency_visits_last_year = Column(Integer, default=0)
    hospitalizations_last_year = Column(Integer, default=0)
    missed_appointments_last_year = Column(Integer, default=0)

    # Digital behavior
    email_open_rate = Column(Float, default=0.0)  # 0.0 to 1.0
    preferred_contact_time = Column(String(50))  # e.g., "morning", "afternoon", "evening"
    preferred_channel = Column(String(50), default="whatsapp")  # whatsapp, email, phone

    # Recommended programs (JSON array of program IDs)
    recommended_programs = Column(JSON, default=list)

    # Metadata
    last_updated = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Relationships
    patient = relationship("Patient", back_populates="digital_twin")

    def __repr__(self):
        return f"<DigitalTwin patient_id={self.patient_id} risk={self.risk_level}>"
