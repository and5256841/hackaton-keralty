# 🗄️ Arquitectura de Base de Datos

## Diseño en Dos Capas

Este proyecto implementa una arquitectura de base de datos en **dos capas lógicas**:

### Capa 1: Base de Datos Transaccional (Operacional)

**Propósito**: Soportar las operaciones del día a día del MVP.

**Tablas**:

#### `patients` - Pacientes
```sql
- id: Integer (PK)
- first_name: String(100)
- last_name: String(100)
- email: String(255) UNIQUE
- phone: String(20)
- date_of_birth: Date
- gender: Enum('M', 'F', 'O')
- city: String(100)
- created_at: DateTime
- updated_at: DateTime
```

#### `digital_twins` - Gemelo Digital Individual
```sql
- id: Integer (PK)
- patient_id: Integer (FK → patients.id) UNIQUE
- risk_level: Enum('healthy', 'susceptible', 'stable_condition', 'high_complexity')
- complication_probability_90d: Float  # 0.0 a 1.0
- estimated_cost_90d: Float  # COP
- conditions: JSON Array  # ["hypertension", "obesity"]
- pending_controls: JSON Array  # ["blood_pressure", "glucose"]
- emergency_visits_last_year: Integer
- hospitalizations_last_year: Integer
- missed_appointments_last_year: Integer
- email_open_rate: Float  # 0.0 a 1.0
- preferred_contact_time: String(50)  # "morning", "afternoon", "evening"
- preferred_channel: String(50)  # "whatsapp", "email", "phone"
- recommended_programs: JSON Array  # ["HYPERTENSION", "OBESITY"]
- last_updated: DateTime
```

#### `programs` - Programas de Salud
```sql
- id: Integer (PK)
- name: String(200)
- code: String(50) UNIQUE  # "HYPERTENSION", "OBESITY", etc.
- description: Text
- target_conditions: JSON Array
- expected_risk_reduction: String(100)
```

#### `chat_sessions` - Sesiones de Chat
```sql
- id: Integer (PK)
- patient_id: Integer (FK → patients.id)
- started_at: DateTime
- ended_at: DateTime (nullable)
- is_active: Boolean
- program_focus: String(100)
```

#### `chat_messages` - Mensajes del Chat
```sql
- id: Integer (PK)
- session_id: Integer (FK → chat_sessions.id)
- role: String(20)  # "user" o "assistant"
- content: Text
- timestamp: DateTime
```

#### `health_goals` - Objetivos de Salud del Paciente
```sql
- id: Integer (PK)
- patient_id: Integer (FK → patients.id)
- title: String(200)
- description: Text
- target_value: String(100)  # "140/90 mmHg"
- current_value: String(100)  # "145/95 mmHg"
- status: Enum('not_started', 'in_progress', 'completed', 'abandoned')
- progress_percentage: Float  # 0.0 a 100.0
- program_code: String(50)
- created_at: DateTime
- target_date: DateTime
- completed_at: DateTime
```

---

### Capa 2: Base de Datos Analítica (Gemelo Poblacional)

**Propósito**: Vista agregada para el asegurador sobre riesgo poblacional e impacto.

**Tablas**:

#### `population_risk_summary` - Resumen de Riesgo Poblacional
```sql
- id: Integer (PK)
- snapshot_date: DateTime
- healthy_count: Integer
- susceptible_count: Integer
- stable_condition_count: Integer
- high_complexity_count: Integer
- total_patients: Integer
- enrolled_in_programs: Integer
- enrollment_rate: Float  # Porcentaje
- avg_email_open_rate: Float
- avg_chat_interactions: Float
- avg_complication_probability: Float
- total_estimated_cost_90d: Float  # Total en COP
- potential_cost_savings: Float  # Si se adoptan programas
- program_distribution: JSON  # {"HYPERTENSION": 120, "OBESITY": 95, ...}
```

---

## Relaciones entre Tablas

```
patients (1) ←→ (1) digital_twins
patients (1) ←→ (N) chat_sessions
patients (1) ←→ (N) health_goals

chat_sessions (1) ←→ (N) chat_messages
```

---

## Variables de Entorno para Base de Datos

### Desarrollo Local

```env
DATABASE_URL=postgresql://user:password@localhost:5432/digital_twin_dev
ANALYTICS_DATABASE_URL=postgresql://user:password@localhost:5432/digital_twin_dev
```

En local, ambas pueden apuntar a la misma base de datos.

### Producción (Render)

```env
DATABASE_URL=<provista por Render automáticamente>
ANALYTICS_DATABASE_URL=<misma que DATABASE_URL para MVP>
```

En una implementación futura a escala, la capa analítica podría:
- Ser una base de datos separada (read replica)
- Usar un data warehouse (BigQuery, Snowflake, Redshift)
- Tener pipelines ETL periódicos

---

## Generar Datos Sintéticos

El script `db/seed_synthetic_data.py` genera:

- **300 pacientes** con perfiles variados
- **Distribución realista de riesgo**:
  - 30% Saludable
  - 35% Susceptible
  - 25% Condición Estable
  - 10% Alta Complejidad
- **Condiciones médicas** basadas en nivel de riesgo
- **Objetivos de salud** personalizados (0-3 por paciente)
- **Datos de comportamiento digital** realistas

---

## Queries Útiles

### Ver pacientes de alto riesgo

```sql
SELECT p.first_name, p.last_name, dt.complication_probability_90d, dt.estimated_cost_90d
FROM patients p
JOIN digital_twins dt ON p.id = dt.patient_id
WHERE dt.risk_level = 'high_complexity'
ORDER BY dt.complication_probability_90d DESC;
```

### Ver distribución de programas

```sql
SELECT
    unnest(recommended_programs::text[]) as program,
    COUNT(*) as patient_count
FROM digital_twins
GROUP BY program
ORDER BY patient_count DESC;
```

### Pacientes con mayor riesgo financiero

```sql
SELECT p.first_name, p.last_name, dt.estimated_cost_90d
FROM patients p
JOIN digital_twins dt ON p.id = dt.patient_id
ORDER BY dt.estimated_cost_90d DESC
LIMIT 10;
```

### Efectividad de invitaciones por canal

```sql
SELECT
    dt.preferred_channel,
    AVG(dt.email_open_rate) as avg_open_rate,
    COUNT(*) as patient_count
FROM digital_twins dt
GROUP BY dt.preferred_channel;
```

---

## Migración y Evolución del Esquema

Para cambios futuros en la estructura, se recomienda usar **Alembic**:

```bash
# Instalar Alembic
pip install alembic

# Inicializar
alembic init alembic

# Crear migración
alembic revision --autogenerate -m "Agregar nueva columna"

# Aplicar migración
alembic upgrade head
```

---

## Backup y Restauración

### Backup

```bash
pg_dump -U digital_twin_user -d digital_twin_dev > backup.sql
```

### Restauración

```bash
psql -U digital_twin_user -d digital_twin_dev < backup.sql
```

---

## Índices Recomendados para Producción

```sql
-- Para búsquedas por email
CREATE INDEX idx_patients_email ON patients(email);

-- Para filtros por nivel de riesgo
CREATE INDEX idx_digital_twins_risk ON digital_twins(risk_level);

-- Para búsquedas de chat por paciente
CREATE INDEX idx_chat_sessions_patient ON chat_sessions(patient_id);

-- Para ordenar mensajes de chat
CREATE INDEX idx_chat_messages_session_time ON chat_messages(session_id, timestamp);
```

---

## Escalabilidad Futura

Para escalar más allá del MVP:

1. **Separar bases de datos**:
   - Base transaccional: PostgreSQL en Render
   - Base analítica: Data warehouse en la nube

2. **Implementar caching**:
   - Redis para resumen poblacional
   - Reduce carga en queries agregados

3. **Read replicas**:
   - Para el dashboard del asegurador
   - No impacta operaciones transaccionales

4. **Particionamiento**:
   - Particionar `chat_messages` por fecha
   - Archivar sesiones antiguas

5. **ETL periódico**:
   - Job nocturno que actualiza `population_risk_summary`
   - No calcular en tiempo real para dashboards
