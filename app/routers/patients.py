"""Patient and Digital Twin endpoints"""
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.database import get_db
from app.models.patient import Patient
from app.models.digital_twin import DigitalTwin
from app.models.health_goal import HealthGoal
from app.schemas.patient import PatientResponse, DigitalTwinResponse, PatientWithTwinResponse

router = APIRouter(prefix="/patients", tags=["Patients"])


@router.get("/", response_model=List[PatientResponse])
def list_patients(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """List all patients"""
    patients = db.query(Patient).offset(skip).limit(limit).all()
    return patients


@router.get("/{patient_id}", response_model=PatientWithTwinResponse)
def get_patient(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """Get a specific patient with their digital twin"""
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    digital_twin = db.query(DigitalTwin).filter(DigitalTwin.patient_id == patient_id).first()

    return PatientWithTwinResponse(
        patient=patient,
        digital_twin=digital_twin
    )


@router.get("/{patient_id}/goals")
def get_patient_goals(
    patient_id: int,
    db: Session = Depends(get_db)
):
    """Get health goals for a patient"""
    patient = db.query(Patient).filter(Patient.id == patient_id).first()

    if not patient:
        raise HTTPException(status_code=404, detail="Patient not found")

    goals = db.query(HealthGoal).filter(HealthGoal.patient_id == patient_id).all()

    return {
        "patient_id": patient_id,
        "goals": [
            {
                "id": goal.id,
                "title": goal.title,
                "description": goal.description,
                "status": goal.status.value,
                "progress_percentage": goal.progress_percentage,
                "target_value": goal.target_value,
                "current_value": goal.current_value,
                "program_code": goal.program_code,
                "target_date": goal.target_date
            }
            for goal in goals
        ]
    }
