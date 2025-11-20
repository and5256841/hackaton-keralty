"""
Admin Router - Healthcare Administration Functions
Includes OCR for medical records (HIPAA-aware MVP)
"""
from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import Dict
import PyPDF2
import io
from datetime import datetime, date

from app.database import get_db
from app.models.patient import Patient
from app.models.digital_twin import DigitalTwin
from app.services.openai_service import openai_service

router = APIRouter(prefix="/admin", tags=["admin"])


@router.post("/upload-historia-clinica")
async def upload_historia_clinica(
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
) -> Dict:
    """
    Upload and process unstructured medical record (PDF).

    ⚠️ HIPAA COMPLIANCE NOTICE:
    This is an MVP demonstration. For production use requires:
    - HIPAA certification
    - End-to-end encryption
    - Data Processing Agreement with OpenAI
    - Audit logging
    - Patient consent management

    Process:
    1. Extract text from PDF (OCR)
    2. Structure data with OpenAI
    3. Create patient record in database
    4. PDF is NOT stored (processed in memory only)
    """

    # Validate file type
    if not file.filename.endswith('.pdf'):
        raise HTTPException(status_code=400, detail="Solo se permiten archivos PDF")

    try:
        # Read PDF content
        pdf_content = await file.read()
        pdf_file = io.BytesIO(pdf_content)

        # Extract text from PDF
        pdf_reader = PyPDF2.PdfReader(pdf_file)
        extracted_text = ""

        for page in pdf_reader.pages:
            extracted_text += page.extract_text() + "\n"

        if not extracted_text.strip():
            raise HTTPException(
                status_code=400,
                detail="No se pudo extraer texto del PDF. Asegúrese de que no sea una imagen escaneada."
            )

        # Structure medical data with OpenAI
        structured_data = await structure_medical_record(extracted_text)

        # Create patient in database
        # Default date_of_birth to 1990-01-01 if not provided (required field in DB)
        dob_str = structured_data.get("date_of_birth")
        if dob_str is None or dob_str == "null":
            dob = date(1990, 1, 1)
        else:
            # Parse string date to Python date object
            try:
                dob = datetime.strptime(dob_str, "%Y-%m-%d").date()
            except (ValueError, TypeError):
                dob = date(1990, 1, 1)

        new_patient = Patient(
            first_name=structured_data.get("first_name", "Desconocido"),
            last_name=structured_data.get("last_name", "Desconocido"),
            email=structured_data.get("email", f"paciente{datetime.now().timestamp()}@example.com"),
            phone=structured_data.get("phone", "+57 300 000 0000"),
            date_of_birth=dob,
            gender=structured_data.get("gender", "O"),
            city=structured_data.get("city", "Bogotá")
        )

        db.add(new_patient)
        db.flush()

        # Create digital twin
        digital_twin = DigitalTwin(
            patient_id=new_patient.id,
            risk_level=structured_data.get("risk_level", "SUSCEPTIBLE"),
            complication_probability_90d=structured_data.get("complication_probability", 0.25),
            estimated_cost_90d=structured_data.get("estimated_cost", 5000000),
            conditions=structured_data.get("conditions", []),
            pending_controls=structured_data.get("pending_controls", 0),
            emergency_visits_last_year=structured_data.get("emergency_visits", 0),
            hospitalizations_last_year=structured_data.get("hospitalizations", 0),
            missed_appointments_last_year=structured_data.get("missed_appointments", 0),
            email_open_rate=0.5,
            preferred_contact_time="morning",
            preferred_channel="whatsapp",
            recommended_programs=structured_data.get("recommended_programs", []),
            last_updated=datetime.now()
        )

        db.add(digital_twin)
        db.commit()
        db.refresh(new_patient)

        return {
            "status": "success",
            "message": "Historia clínica procesada exitosamente",
            "patient_id": new_patient.id,
            "patient_name": f"{new_patient.first_name} {new_patient.last_name}",
            "extracted_data": structured_data,
            "hipaa_notice": "⚠️ PDF procesado en memoria y descartado. Solo datos estructurados almacenados.",
            "next_steps": "Paciente disponible para campaña de WhatsApp"
        }

    except PyPDF2.errors.PdfReadError:
        raise HTTPException(status_code=400, detail="Error al leer el PDF. Archivo corrupto o protegido.")
    except Exception as e:
        db.rollback()
        raise HTTPException(status_code=500, detail=f"Error al procesar historia clínica: {str(e)}")


async def structure_medical_record(raw_text: str) -> Dict:
    """
    Use OpenAI to structure unstructured medical record text.

    Extracts:
    - Patient demographics (name, age, gender, city)
    - Medical conditions
    - Risk level
    - Recommended health programs
    """

    if not openai_service:
        # Fallback if OpenAI not configured
        return {
            "first_name": "Paciente",
            "last_name": "Demo",
            "gender": "O",
            "city": "Bogotá",
            "conditions": ["Pendiente de evaluación"],
            "risk_level": "SUSCEPTIBLE",
            "recommended_programs": ["GENERAL"]
        }

    prompt = f"""Analiza esta historia clínica y extrae SOLO la información estructurada en formato JSON.

HISTORIA CLÍNICA:
{raw_text[:3000]}  # Limit to 3000 chars for token limits

Extrae y retorna EXACTAMENTE este JSON (si no encuentras un dato, usa null):
{{
    "first_name": "Nombre del paciente",
    "last_name": "Apellido del paciente",
    "date_of_birth": "YYYY-MM-DD o null",
    "gender": "M, F o O",
    "city": "Ciudad (Bogotá, Medellín, Cali, etc)",
    "email": null,
    "phone": "Teléfono o null",
    "conditions": ["Lista de condiciones médicas encontradas"],
    "risk_level": "HEALTHY, SUSCEPTIBLE, STABLE_CONDITION o HIGH_COMPLEXITY",
    "complication_probability": 0.0-1.0,
    "estimated_cost": número estimado,
    "pending_controls": número de controles pendientes,
    "emergency_visits": número de visitas a urgencias,
    "hospitalizations": número de hospitalizaciones,
    "missed_appointments": número de citas perdidas,
    "recommended_programs": ["HYPERTENSION", "DIABETES", "OBESITY", "CARDIOVASCULAR", "PRENATAL"]
}}

IMPORTANTE:
- Retorna SOLO el JSON, sin texto adicional
- Si no encuentras un dato, usa null
- Para risk_level usa exactamente uno de los 4 valores listados
- Para recommended_programs usa los códigos exactos listados
"""

    try:
        from openai import OpenAI
        client = openai_service.client

        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": "Eres un asistente médico que extrae datos estructurados de historias clínicas. Retorna SOLO JSON válido."},
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            max_tokens=1000
        )

        import json
        structured_data = json.loads(response.choices[0].message.content)

        return structured_data

    except Exception as e:
        # Fallback on error
        print(f"Error structuring medical record: {e}")
        return {
            "first_name": "Paciente",
            "last_name": "Procesado",
            "gender": "O",
            "city": "Bogotá",
            "conditions": ["Información pendiente de validación"],
            "risk_level": "SUSCEPTIBLE",
            "recommended_programs": ["GENERAL"]
        }
