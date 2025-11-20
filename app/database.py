"""
Database connection and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.config import settings

# Create database engines
engine = create_engine(settings.database_url, echo=settings.debug)
analytics_engine = create_engine(settings.analytics_database_url, echo=False)

# Create session factories
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
AnalyticsSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=analytics_engine)

# Base class for models
Base = declarative_base()


def get_db():
    """Dependency for getting database session"""
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_analytics_db():
    """Dependency for getting analytics database session"""
    db = AnalyticsSessionLocal()
    try:
        yield db
    finally:
        db.close()
