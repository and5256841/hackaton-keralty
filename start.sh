#!/bin/bash
# Startup script for Render deployment
# Initializes database and starts the FastAPI application

echo "🚀 Starting Digital Twin Health API..."

# Check if DATABASE_URL is set (PostgreSQL in production)
if [ -n "$DATABASE_URL" ]; then
    echo "📊 PostgreSQL detected. Initializing database..."

    # Initialize database schema (safe - won't recreate if exists)
    python db/init_db.py 2>&1 || echo "⚠️  Database schema already exists"

    # Seed synthetic data ONLY if not already seeded
    # This prevents duplicate data on restart
    python -c "
from app.database import SessionLocal
from app.models import Patient
db = SessionLocal()
try:
    count = db.query(Patient).count()
    if count == 0:
        print('📝 Database is empty, seeding synthetic data...')
        import subprocess
        subprocess.run(['python', 'db/seed_synthetic_data.py'])
    else:
        print(f'✅ Database already has {count} patients, skipping seed')
finally:
    db.close()
" 2>&1 || echo "⚠️  Data seeding check skipped"
else
    echo "📁 Using SQLite for local development"

    # Check if SQLite database exists
    if [ ! -f "./digital_twin.db" ]; then
        echo "Creating SQLite database..."
        python db/init_db.py
        python db/seed_synthetic_data.py
    fi
fi

echo "✅ Database ready!"
echo "🌐 Starting web server..."

# Start the FastAPI application with production settings
# --workers 1: Single worker for free tier (512MB RAM limit)
# --timeout-keep-alive 5: Reduce memory from idle connections
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000} --workers 1 --timeout-keep-alive 5
