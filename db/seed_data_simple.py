"""
Seed database with 300 synthetic patients - Windows compatible version
"""
import sys
import os
import random
from datetime import datetime, timedelta

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models.patient import Patient, Gender
from app.models.digital_twin import DigitalTwin, RiskLevel
from app.models.program import Program
from app.models.health_goal import HealthGoal, GoalStatus

# Fake data for Spanish/LATAM
FIRST_NAMES_MALE = ["Juan", "Carlos", "Luis", "Miguel", "Pedro", "Jose", "Antonio", "Francisco", "Jorge", "Diego"]
FIRST_NAMES_FEMALE = ["Maria", "Ana", "Carmen", "Lucia", "Isabel", "Sofia", "Elena", "Paula", "Laura", "Patricia"]
LAST_NAMES = ["Garcia", "Martinez", "Rodriguez", "Lopez", "Gonzalez", "Fernandez", "Sanchez", "Perez", "Torres", "Ramirez"]

CITIES = ["Bogota", "Medellin", "Cali", "Barranquilla", "Cartagena", "Bucaramanga", "Pereira", "Manizales"]

PROGRAMS = [
    {
        "name": "Programa de Hipertension",
        "code": "HYPERTENSION",
        "description": "Control y seguimiento de pacientes con hipertension arterial",
        "target_conditions": ["hypertension", "pre_hypertension"],
        "expected_risk_reduction": "30-40% reduccion en complicaciones cardiovasculares"
    },
    {
        "name": "Programa de Obesidad y Nutricion",
        "code": "OBESITY",
        "description": "Apoyo integral para manejo de peso y habitos alimenticios",
        "target_conditions": ["obesity", "overweight"],
        "expected_risk_reduction": "25-35% reduccion en riesgo metabolico"
    },
    {
        "name": "Programa Prenatal",
        "code": "PRENATAL",
        "description": "Seguimiento y cuidado durante el embarazo",
        "target_conditions": ["pregnancy", "high_risk_pregnancy"],
        "expected_risk_reduction": "40-50% reduccion en complicaciones del embarazo"
    },
    {
        "name": "Programa de Diabetes",
        "code": "DIABETES",
        "description": "Control integral de diabetes tipo 1 y 2",
        "target_conditions": ["diabetes", "pre_diabetes"],
        "expected_risk_reduction": "35-45% reduccion en complicaciones diabeticas"
    },
    {
        "name": "Programa Cardiovascular",
        "code": "CARDIOVASCULAR",
        "description": "Prevencion y manejo de enfermedades cardiovasculares",
        "target_conditions": ["heart_disease", "high_cholesterol"],
        "expected_risk_reduction": "30-40% reduccion en eventos cardiovasculares"
    }
]

CONDITIONS = ["hypertension", "obesity", "diabetes", "pre_diabetes", "high_cholesterol", "overweight"]
CONTROLS = ["blood_pressure", "glucose", "cholesterol", "weight", "eye_exam", "kidney_function"]


def generate_programs(db):
    print("[*] Creating health programs...")
    for prog_data in PROGRAMS:
        program = Program(**prog_data)
        db.add(program)
    db.commit()
    print(f"[OK] Created {len(PROGRAMS)} programs")


def generate_patients(db, count=300):
    print(f"[*] Generating {count} synthetic patients...")

    for i in range(count):
        gender = random.choice(list(Gender))

        if gender == Gender.MALE:
            first_name = random.choice(FIRST_NAMES_MALE)
        else:
            first_name = random.choice(FIRST_NAMES_FEMALE)

        last_name = random.choice(LAST_NAMES)
        age = random.randint(18, 80)
        dob = datetime.now().date() - timedelta(days=age * 365)

        patient = Patient(
            first_name=first_name,
            last_name=last_name,
            email=f"{first_name.lower()}.{last_name.lower()}{i}@example.com",
            phone=f"+57{random.randint(3000000000, 3999999999)}",
            date_of_birth=dob,
            gender=gender,
            city=random.choice(CITIES)
        )

        db.add(patient)
        db.flush()

        # Determine risk level
        risk_choices = [
            (RiskLevel.HEALTHY, 0.30),
            (RiskLevel.SUSCEPTIBLE, 0.35),
            (RiskLevel.STABLE_CONDITION, 0.25),
            (RiskLevel.HIGH_COMPLEXITY, 0.10)
        ]
        risk_level = random.choices([r[0] for r in risk_choices], weights=[r[1] for r in risk_choices])[0]

        # Generate conditions based on risk
        num_conditions = {
            RiskLevel.HEALTHY: 0,
            RiskLevel.SUSCEPTIBLE: random.randint(1, 2),
            RiskLevel.STABLE_CONDITION: random.randint(1, 3),
            RiskLevel.HIGH_COMPLEXITY: random.randint(2, 4)
        }[risk_level]

        patient_conditions = random.sample(CONDITIONS, min(num_conditions, len(CONDITIONS)))

        complication_prob = {
            RiskLevel.HEALTHY: random.uniform(0.01, 0.05),
            RiskLevel.SUSCEPTIBLE: random.uniform(0.10, 0.25),
            RiskLevel.STABLE_CONDITION: random.uniform(0.25, 0.45),
            RiskLevel.HIGH_COMPLEXITY: random.uniform(0.50, 0.80)
        }[risk_level]

        estimated_cost = complication_prob * random.uniform(5000000, 15000000)

        num_pending = random.randint(0, min(3, len(CONTROLS)))
        pending = random.sample(CONTROLS, num_pending)

        email_open_rate = random.uniform(0.1, 0.9)
        preferred_time = random.choice(["morning", "afternoon", "evening"])
        preferred_channel = random.choice(["whatsapp", "email", "phone"])

        recommended = []
        for condition in patient_conditions:
            for prog in PROGRAMS:
                if condition in prog["target_conditions"]:
                    recommended.append(prog["code"])

        digital_twin = DigitalTwin(
            patient_id=patient.id,
            risk_level=risk_level,
            complication_probability_90d=round(complication_prob, 3),
            estimated_cost_90d=round(estimated_cost, 2),
            conditions=patient_conditions,
            pending_controls=pending,
            emergency_visits_last_year=random.randint(0, 5) if risk_level in [RiskLevel.STABLE_CONDITION, RiskLevel.HIGH_COMPLEXITY] else 0,
            hospitalizations_last_year=random.randint(0, 2) if risk_level == RiskLevel.HIGH_COMPLEXITY else 0,
            missed_appointments_last_year=random.randint(0, 3),
            email_open_rate=round(email_open_rate, 2),
            preferred_contact_time=preferred_time,
            preferred_channel=preferred_channel,
            recommended_programs=list(set(recommended))
        )

        db.add(digital_twin)

        if (i + 1) % 50 == 0:
            print(f"  ... {i + 1}/{count} patients created")
            db.commit()

    db.commit()
    print(f"[OK] Created {count} patients with digital twins")


def seed_database():
    print("\n[*] Starting database seeding...\n")

    db = SessionLocal()

    try:
        generate_programs(db)
        generate_patients(db, count=300)

        print("\n[OK] Database seeding completed successfully!")
        print("[*] Ready for demo!\n")

    except Exception as e:
        print(f"\n[ERROR] Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
