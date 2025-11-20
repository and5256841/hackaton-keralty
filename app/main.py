"""
Digital Twin Health MVP - Main FastAPI Application
"""
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
import os

from app.config import settings
from app.routers import chat, patients, analytics

# Create FastAPI app
app = FastAPI(
    title=settings.app_name,
    version=settings.app_version,
    description="MVP platform for personalized health program invitations using digital twins"
)

# CORS middleware (allow frontend to call API)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, specify exact origins
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include routers
app.include_router(chat.router)
app.include_router(patients.router)
app.include_router(analytics.router)

# Serve static files (CSS, JS, images)
if os.path.exists("static"):
    app.mount("/static", StaticFiles(directory="static"), name="static")

# Serve frontend HTML files
@app.get("/")
def root():
    """Root endpoint - redirect to chat"""
    return {"message": "Digital Twin Health MVP API", "docs": "/docs"}


@app.get("/chat-ui")
def serve_chat():
    """Serve chat frontend"""
    return FileResponse("frontend/chat.html")


@app.get("/patient-dashboard")
def serve_patient_dashboard():
    """Serve patient dashboard"""
    return FileResponse("frontend/patient_dashboard.html")


@app.get("/insurer-platform")
def serve_insurer_platform():
    """Serve insurer management platform"""
    return FileResponse("frontend/insurer_platform.html")


@app.get("/health")
def health_check():
    """Health check endpoint"""
    return {
        "status": "healthy",
        "app": settings.app_name,
        "version": settings.app_version,
        "openai_configured": bool(settings.openai_api_key)
    }


@app.get("/setup-database")
def setup_database():
    """
    ONE-TIME endpoint to initialize database with synthetic data.
    Visit this URL once to setup the database, then it can be removed.
    """
    try:
        import subprocess

        # Run init_db.py
        result_init = subprocess.run(
            ["python", "db/init_db.py"],
            capture_output=True,
            text=True,
            timeout=30
        )

        # Run seed_synthetic_data.py
        result_seed = subprocess.run(
            ["python", "db/seed_synthetic_data.py"],
            capture_output=True,
            text=True,
            timeout=120
        )

        return {
            "status": "success",
            "message": "Database initialized successfully",
            "init_output": result_init.stdout,
            "seed_output": result_seed.stdout,
            "note": "You can now remove this endpoint for security"
        }
    except Exception as e:
        return {
            "status": "error",
            "message": str(e),
            "note": "If this fails, use Render Shell to run: python db/init_db.py && python db/seed_synthetic_data.py"
        }


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
