"""Pydantic schemas for patient and digital twin"""
from pydantic import BaseModel
from datetime import date, datetime
from typing import List, Optional


class PatientBase(BaseModel):
    """Base patient info"""
    first_name: str
    last_name: str
    email: str
    date_of_birth: date
    gender: str
    city: Optional[str] = None


class PatientResponse(PatientBase):
    """Patient response with ID"""
    id: int
    created_at: datetime

    class Config:
        from_attributes = True


class DigitalTwinResponse(BaseModel):
    """Digital twin data"""
    id: int
    patient_id: int
    risk_level: str
    complication_probability_90d: float
    estimated_cost_90d: float
    conditions: List[str]
    pending_controls: List[str]
    emergency_visits_last_year: int
    recommended_programs: List[str]
    email_open_rate: float
    preferred_contact_time: Optional[str] = None
    preferred_channel: str

    class Config:
        from_attributes = True


class PatientWithTwinResponse(BaseModel):
    """Patient with their digital twin"""
    patient: PatientResponse
    digital_twin: Optional[DigitalTwinResponse] = None

    class Config:
        from_attributes = True
