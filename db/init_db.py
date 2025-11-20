"""
Initialize database - Create all tables
Run this script to set up the database schema
"""
import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import engine, Base
from app.models import (
    Patient,
    DigitalTwin,
    Program,
    ChatSession,
    ChatMessage,
    HealthGoal,
    PopulationRiskSummary
)


def init_database():
    """Create all tables in the database"""
    print("[*] Creating database tables...")

    try:
        Base.metadata.create_all(bind=engine)
        print("[OK] Database tables created successfully!")
        print("\nCreated tables:")
        for table in Base.metadata.sorted_tables:
            print(f"  - {table.name}")

    except Exception as e:
        print(f"[ERROR] Error creating database: {e}")
        raise


if __name__ == "__main__":
    init_database()
