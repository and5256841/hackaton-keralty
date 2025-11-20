"""Analytics models - Population-level insights for the insurer"""
from sqlalchemy import Column, Integer, String, Float, DateTime, JSON
from datetime import datetime
from app.database import Base


class PopulationRiskSummary(Base):
    """
    Aggregated population risk data - 'Gemelo Poblacional'
    This is what the insurer sees in their management dashboard
    """
    __tablename__ = "population_risk_summary"

    id = Column(Integer, primary_key=True, index=True)

    # Snapshot metadata
    snapshot_date = Column(DateTime, default=datetime.utcnow)

    # Population counts by risk level
    healthy_count = Column(Integer, default=0)
    susceptible_count = Column(Integer, default=0)
    stable_condition_count = Column(Integer, default=0)
    high_complexity_count = Column(Integer, default=0)

    # Program enrollment
    total_patients = Column(Integer, default=0)
    enrolled_in_programs = Column(Integer, default=0)
    enrollment_rate = Column(Float, default=0.0)  # Percentage

    # Digital engagement metrics
    avg_email_open_rate = Column(Float, default=0.0)
    avg_chat_interactions = Column(Float, default=0.0)

    # Clinical outcomes
    avg_complication_probability = Column(Float, default=0.0)
    total_estimated_cost_90d = Column(Float, default=0.0)  # Total cost if no intervention
    potential_cost_savings = Column(Float, default=0.0)  # If programs are adopted

    # Program-specific breakdown (JSON)
    program_distribution = Column(JSON, default=dict)  # {program_code: patient_count}

    def __repr__(self):
        return f"<PopulationRiskSummary date={self.snapshot_date} total={self.total_patients}>"
