#!/bin/bash
# Startup script for Render deployment
# Initializes database and starts the FastAPI application

set -e  # Exit on error

echo "🚀 Starting Digital Twin Health API..."

# Check if DATABASE_URL is set (PostgreSQL in production)
if [ -n "$DATABASE_URL" ]; then
    echo "📊 PostgreSQL detected. Initializing database..."

    # Initialize database schema
    python db/init_db.py || echo "⚠️  Database init failed or already initialized"

    # Seed synthetic data (only if database is empty)
    python db/seed_synthetic_data.py || echo "⚠️  Data seeding skipped or already done"
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

# Start the FastAPI application
exec uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}
