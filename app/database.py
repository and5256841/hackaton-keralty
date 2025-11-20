"""
Database connection and session management
"""
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import NullPool
from app.config import settings

# Engine configuration for production stability
engine_config = {
    "echo": settings.debug,
    "pool_pre_ping": True,  # Verify connections before using
    "pool_recycle": 300,     # Recycle connections after 5 minutes
}

# Use NullPool for SQLite to avoid locking issues
if settings.database_url.startswith("sqlite"):
    engine_config["connect_args"] = {"check_same_thread": False}
    engine_config["poolclass"] = NullPool
else:
    # PostgreSQL connection pooling
    engine_config["pool_size"] = 5
    engine_config["max_overflow"] = 10

# Create database engines
engine = create_engine(settings.database_url, **engine_config)

# Analytics engine (simplified config)
analytics_config = {
    "echo": False,
    "pool_pre_ping": True,
}
if settings.analytics_database_url.startswith("sqlite"):
    analytics_config["connect_args"] = {"check_same_thread": False}
    analytics_config["poolclass"] = NullPool
else:
    analytics_config["pool_size"] = 3
    analytics_config["max_overflow"] = 5

analytics_engine = create_engine(settings.analytics_database_url, **analytics_config)

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
