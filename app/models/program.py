"""Health Program model"""
from sqlalchemy import Column, Integer, String, Text, JSON
from app.database import Base


class Program(Base):
    """Health programs offered by the insurer"""
    __tablename__ = "programs"

    id = Column(Integer, primary_key=True, index=True)

    # Program details
    name = Column(String(200), nullable=False)
    code = Column(String(50), unique=True, index=True)  # e.g., "HYPERTENSION", "OBESITY"
    description = Column(Text)

    # Target conditions this program addresses
    target_conditions = Column(JSON, default=list)  # e.g., ["hypertension", "pre_hypertension"]

    # Expected outcomes
    expected_risk_reduction = Column(String(100))  # e.g., "30-40% reduction in complications"

    def __repr__(self):
        return f"<Program {self.code}>"
