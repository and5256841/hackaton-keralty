"""Pydantic schemas for analytics/insurer dashboard"""
from pydantic import BaseModel
from typing import Dict


class PopulationSummaryResponse(BaseModel):
    """Population-level summary for insurer dashboard"""
    total_patients: int
    healthy_count: int
    susceptible_count: int
    stable_condition_count: int
    high_complexity_count: int
    enrolled_in_programs: int
    enrollment_rate: float
    avg_email_open_rate: float
    avg_complication_probability: float
    total_estimated_cost_90d: float
    potential_cost_savings: float
    program_distribution: Dict[str, int]

    class Config:
        from_attributes = True
