"""
Seed database with 300 synthetic patients
Generates realistic but fake data for demo purposes
"""
import sys
import os
import random
from datetime import datetime, timedelta
from faker import Faker

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from app.database import SessionLocal
from app.models.patient import Patient, Gender
from app.models.digital_twin import DigitalTwin, RiskLevel
from app.models.program import Program
from app.models.health_goal import HealthGoal, GoalStatus

# Initialize Faker for Spanish (Colombia/LATAM)
fake = Faker(['es_CO', 'es_MX'])

# Health programs offered
PROGRAMS = [
    {
        "name": "Programa de Hipertensión",
        "code": "HYPERTENSION",
        "description": "Control y seguimiento de pacientes con hipertensión arterial",
        "target_conditions": ["hypertension", "pre_hypertension"],
        "expected_risk_reduction": "30-40% reducción en complicaciones cardiovasculares"
    },
    {
        "name": "Programa de Obesidad y Nutrición",
        "code": "OBESITY",
        "description": "Apoyo integral para manejo de peso y hábitos alimenticios",
        "target_conditions": ["obesity", "overweight"],
        "expected_risk_reduction": "25-35% reducción en riesgo metabólico"
    },
    {
        "name": "Programa Prenatal",
        "code": "PRENATAL",
        "description": "Seguimiento y cuidado durante el embarazo",
        "target_conditions": ["pregnancy", "high_risk_pregnancy"],
        "expected_risk_reduction": "40-50% reducción en complicaciones del embarazo"
    },
    {
        "name": "Programa de Diabetes",
        "code": "DIABETES",
        "description": "Control integral de diabetes tipo 1 y 2",
        "target_conditions": ["diabetes", "pre_diabetes"],
        "expected_risk_reduction": "35-45% reducción en complicaciones diabéticas"
    },
    {
        "name": "Programa Cardiovascular",
        "code": "CARDIOVASCULAR",
        "description": "Prevención y manejo de enfermedades cardiovasculares",
        "target_conditions": ["heart_disease", "high_cholesterol"],
        "expected_risk_reduction": "30-40% reducción en eventos cardiovasculares"
    }
]

# Colombian cities
CITIES = [
    "Bogotá", "Medellín", "Cali", "Barranquilla", "Cartagena",
    "Bucaramanga", "Pereira", "Manizales", "Ibagué", "Santa Marta"
]

# Possible health conditions
CONDITIONS = [
    "hypertension", "obesity", "diabetes", "pre_diabetes",
    "high_cholesterol", "overweight", "pregnancy"
]

# Pending medical controls
CONTROLS = [
    "blood_pressure", "glucose", "cholesterol", "weight",
    "prenatal_checkup", "eye_exam", "kidney_function"
]


def random_date_of_birth():
    """Generate random date of birth (18-80 years old)"""
    age = random.randint(18, 80)
    return datetime.now().date() - timedelta(days=age * 365)


def generate_programs(db):
    """Create health programs"""
    print("📋 Creating health programs...")
    programs_created = []

    for prog_data in PROGRAMS:
        program = Program(**prog_data)
        db.add(program)
        programs_created.append(program)

    db.commit()
    print(f"✅ Created {len(programs_created)} programs")
    return programs_created


def generate_patients(db, count=300):
    """Generate synthetic patients with digital twins"""
    print(f"👥 Generating {count} synthetic patients...")

    patients_created = []

    for i in range(count):
        # Create patient
        gender = random.choice(list(Gender))

        patient = Patient(
            first_name=fake.first_name_male() if gender == Gender.MALE else fake.first_name_female(),
            last_name=fake.last_name(),
            email=fake.unique.email(),
            phone=fake.phone_number(),
            date_of_birth=random_date_of_birth(),
            gender=gender,
            city=random.choice(CITIES)
        )

        db.add(patient)
        db.flush()  # Get patient.id

        # Determine risk level with realistic distribution
        risk_distribution = [
            (RiskLevel.HEALTHY, 0.30),
            (RiskLevel.SUSCEPTIBLE, 0.35),
            (RiskLevel.STABLE_CONDITION, 0.25),
            (RiskLevel.HIGH_COMPLEXITY, 0.10)
        ]
        risk_level = random.choices(
            [r[0] for r in risk_distribution],
            weights=[r[1] for r in risk_distribution]
        )[0]

        # Generate conditions based on risk level
        num_conditions = {
            RiskLevel.HEALTHY: 0,
            RiskLevel.SUSCEPTIBLE: random.randint(1, 2),
            RiskLevel.STABLE_CONDITION: random.randint(1, 3),
            RiskLevel.HIGH_COMPLEXITY: random.randint(2, 4)
        }[risk_level]

        patient_conditions = random.sample(CONDITIONS, min(num_conditions, len(CONDITIONS)))

        # Complication probability based on risk
        complication_prob = {
            RiskLevel.HEALTHY: random.uniform(0.01, 0.05),
            RiskLevel.SUSCEPTIBLE: random.uniform(0.10, 0.25),
            RiskLevel.STABLE_CONDITION: random.uniform(0.25, 0.45),
            RiskLevel.HIGH_COMPLEXITY: random.uniform(0.50, 0.80)
        }[risk_level]

        # Estimated cost (higher risk = higher cost)
        estimated_cost = complication_prob * random.uniform(5000000, 15000000)  # COP

        # Pending controls
        num_pending = random.randint(0, min(3, len(CONTROLS)))
        pending = random.sample(CONTROLS, num_pending)

        # Digital behavior
        email_open_rate = random.uniform(0.1, 0.9)
        preferred_time = random.choice(["morning", "afternoon", "evening"])
        preferred_channel = random.choice(["whatsapp", "email", "phone"])

        # Recommended programs based on conditions
        recommended = []
        for condition in patient_conditions:
            for prog in PROGRAMS:
                if condition in prog["target_conditions"]:
                    recommended.append(prog["code"])

        # Create digital twin
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

        # Create health goals for patients with conditions
        if patient_conditions:
            num_goals = random.randint(1, 3)
            goals = generate_health_goals_for_patient(patient.id, patient_conditions, num_goals)
            for goal in goals:
                db.add(goal)

        patients_created.append(patient)

        if (i + 1) % 50 == 0:
            print(f"  ... {i + 1}/{count} patients created")

    db.commit()
    print(f"✅ Created {len(patients_created)} patients with digital twins")
    return patients_created


def generate_health_goals_for_patient(patient_id, conditions, num_goals):
    """Generate health goals based on patient conditions"""
    goals = []

    goal_templates = {
        "hypertension": {
            "title": "Controlar presión arterial",
            "description": "Mantener presión arterial por debajo de 140/90 mmHg",
            "target_value": "130/80 mmHg",
            "current_value": "145/95 mmHg",
            "program_code": "HYPERTENSION"
        },
        "obesity": {
            "title": "Alcanzar peso saludable",
            "description": "Reducir IMC a rango saludable",
            "target_value": "25 IMC",
            "current_value": "32 IMC",
            "program_code": "OBESITY"
        },
        "diabetes": {
            "title": "Control de glucosa",
            "description": "Mantener niveles de glucosa en ayunas normales",
            "target_value": "100 mg/dL",
            "current_value": "145 mg/dL",
            "program_code": "DIABETES"
        }
    }

    for condition in conditions[:num_goals]:
        if condition in goal_templates:
            template = goal_templates[condition]
            status = random.choice(list(GoalStatus))
            progress = {
                GoalStatus.NOT_STARTED: 0.0,
                GoalStatus.IN_PROGRESS: random.uniform(10, 70),
                GoalStatus.COMPLETED: 100.0,
                GoalStatus.ABANDONED: random.uniform(5, 40)
            }[status]

            goal = HealthGoal(
                patient_id=patient_id,
                title=template["title"],
                description=template["description"],
                target_value=template["target_value"],
                current_value=template["current_value"],
                status=status,
                progress_percentage=round(progress, 1),
                program_code=template["program_code"],
                target_date=datetime.now() + timedelta(days=random.randint(30, 180))
            )
            goals.append(goal)

    return goals


def seed_database():
    """Main seeding function"""
    print("\n🌱 Starting database seeding...\n")

    db = SessionLocal()

    try:
        # Create programs
        generate_programs(db)

        # Create patients with digital twins
        generate_patients(db, count=300)

        print("\n✅ Database seeding completed successfully!")
        print("🎉 Ready for demo!\n")

    except Exception as e:
        print(f"\n❌ Error seeding database: {e}")
        db.rollback()
        raise
    finally:
        db.close()


if __name__ == "__main__":
    seed_database()
