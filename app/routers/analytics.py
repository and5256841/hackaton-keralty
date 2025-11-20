"""Analytics endpoints for insurer dashboard"""
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func
from typing import Dict

from app.database import get_db
from app.models.patient import Patient
from app.models.digital_twin import DigitalTwin, RiskLevel
from app.schemas.analytics import PopulationSummaryResponse

router = APIRouter(prefix="/analytics", tags=["Analytics"])


@router.get("/population-summary", response_model=PopulationSummaryResponse)
def get_population_summary(db: Session = Depends(get_db)):
    """
    Get population-level summary for insurer dashboard
    This is the 'gemelo poblacional' view
    """

    # Total patients
    total_patients = db.query(func.count(Patient.id)).scalar()

    # Counts by risk level
    risk_counts = db.query(
        DigitalTwin.risk_level,
        func.count(DigitalTwin.id)
    ).group_by(DigitalTwin.risk_level).all()

    risk_dict = {risk.value: count for risk, count in risk_counts}

    healthy_count = risk_dict.get(RiskLevel.HEALTHY.value, 0)
    susceptible_count = risk_dict.get(RiskLevel.SUSCEPTIBLE.value, 0)
    stable_condition_count = risk_dict.get(RiskLevel.STABLE_CONDITION.value, 0)
    high_complexity_count = risk_dict.get(RiskLevel.HIGH_COMPLEXITY.value, 0)

    # Patients with recommended programs (enrolled in programs)
    enrolled_count = db.query(func.count(DigitalTwin.id)).filter(
        func.json_array_length(DigitalTwin.recommended_programs) > 0
    ).scalar()

    enrollment_rate = (enrolled_count / total_patients * 100) if total_patients > 0 else 0

    # Average email open rate
    avg_open_rate = db.query(func.avg(DigitalTwin.email_open_rate)).scalar() or 0

    # Average complication probability
    avg_complication = db.query(func.avg(DigitalTwin.complication_probability_90d)).scalar() or 0

    # Total estimated cost (if no intervention)
    total_cost = db.query(func.sum(DigitalTwin.estimated_cost_90d)).scalar() or 0

    # Potential savings (assume 35% reduction if programs adopted)
    potential_savings = total_cost * 0.35

    # Program distribution
    # Get all digital twins with recommended programs
    twins = db.query(DigitalTwin).all()
    program_dist: Dict[str, int] = {}

    for twin in twins:
        if twin.recommended_programs:
            for prog in twin.recommended_programs:
                program_dist[prog] = program_dist.get(prog, 0) + 1

    return PopulationSummaryResponse(
        total_patients=total_patients,
        healthy_count=healthy_count,
        susceptible_count=susceptible_count,
        stable_condition_count=stable_condition_count,
        high_complexity_count=high_complexity_count,
        enrolled_in_programs=enrolled_count,
        enrollment_rate=round(enrollment_rate, 2),
        avg_email_open_rate=round(avg_open_rate, 3),
        avg_complication_probability=round(avg_complication, 3),
        total_estimated_cost_90d=round(total_cost, 2),
        potential_cost_savings=round(potential_savings, 2),
        program_distribution=program_dist
    )


@router.get("/patients-by-risk")
def get_patients_by_risk(
    risk_level: str,
    skip: int = 0,
    limit: int = 50,
    db: Session = Depends(get_db)
):
    """Get patients filtered by risk level"""

    try:
        risk_enum = RiskLevel(risk_level)
    except ValueError:
        return {"error": f"Invalid risk level. Valid values: {[r.value for r in RiskLevel]}"}

    twins = db.query(DigitalTwin).filter(
        DigitalTwin.risk_level == risk_enum
    ).offset(skip).limit(limit).all()

    patients_data = []
    for twin in twins:
        patient = db.query(Patient).filter(Patient.id == twin.patient_id).first()
        if patient:
            patients_data.append({
                "patient_id": patient.id,
                "name": f"{patient.first_name} {patient.last_name}",
                "age": (2024 - patient.date_of_birth.year),
                "city": patient.city,
                "risk_level": twin.risk_level.value,
                "complication_probability_90d": twin.complication_probability_90d,
                "estimated_cost_90d": twin.estimated_cost_90d,
                "conditions": twin.conditions,
                "recommended_programs": twin.recommended_programs
            })

    return {
        "risk_level": risk_level,
        "count": len(patients_data),
        "patients": patients_data
    }
