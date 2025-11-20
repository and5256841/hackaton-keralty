# ⚡ Guía de Inicio Rápido

**Tienes el proyecto listo. Sigue estos pasos para ejecutarlo en 10 minutos.**

---

## ✅ Checklist Pre-requisitos

Antes de empezar, asegúrate de tener:

- [ ] Python 3.11 o superior instalado
- [ ] PostgreSQL 14+ instalado y corriendo
- [ ] API key de OpenAI (obtener en https://platform.openai.com/api-keys)
- [ ] Git instalado (opcional, para clonar)

---

## 🚀 Pasos de Instalación

### 1️⃣ Crear entorno virtual

```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Linux/Mac
python3 -m venv venv
source venv/bin/activate
```

Verás `(venv)` al inicio de tu terminal.

---

### 2️⃣ Instalar dependencias

```bash
pip install -r requirements.txt
```

Esto instalará:
- FastAPI
- SQLAlchemy
- OpenAI
- Faker (para datos sintéticos)
- Y otras dependencias necesarias

---

### 3️⃣ Configurar PostgreSQL

**Opción A: PostgreSQL Local**

```sql
-- Abre psql o pgAdmin y ejecuta:
CREATE DATABASE digital_twin_dev;
CREATE USER digital_twin_user WITH PASSWORD 'tu_password_aqui';
GRANT ALL PRIVILEGES ON DATABASE digital_twin_dev TO digital_twin_user;
```

**Opción B: PostgreSQL en Docker**

```bash
docker run --name digital-twin-postgres \
  -e POSTGRES_PASSWORD=tu_password \
  -e POSTGRES_USER=digital_twin_user \
  -e POSTGRES_DB=digital_twin_dev \
  -p 5432:5432 \
  -d postgres:14
```

---

### 4️⃣ Configurar variables de entorno

```bash
# Copiar archivo de ejemplo
cp .env.example .env

# Editar .env con tu editor favorito
notepad .env   # Windows
nano .env      # Linux/Mac
```

**Edita estas líneas en `.env`:**

```env
# ⚠️ IMPORTANTE: Reemplaza con tu API key real
OPENAI_API_KEY=sk-tu-api-key-de-openai-aqui

# Ajusta con tu password de PostgreSQL
DATABASE_URL=postgresql://digital_twin_user:tu_password_aqui@localhost:5432/digital_twin_dev

# Esta puede ser igual a DATABASE_URL para el MVP
ANALYTICS_DATABASE_URL=postgresql://digital_twin_user:tu_password_aqui@localhost:5432/digital_twin_dev
```

**¿Dónde conseguir tu OpenAI API key?**
1. Ve a https://platform.openai.com/api-keys
2. Click en "Create new secret key"
3. Copia la key (empieza con `sk-`)
4. Pégala en tu `.env`

---

### 5️⃣ Inicializar la base de datos

```bash
# Crear tablas
python db/init_db.py

# Generar 300 pacientes sintéticos
python db/seed_synthetic_data.py
```

Deberías ver:

```
🔧 Creating database tables...
✅ Database tables created successfully!

🌱 Starting database seeding...
📋 Creating health programs...
✅ Created 5 programs
👥 Generating 300 synthetic patients...
  ... 50/300 patients created
  ... 100/300 patients created
  ... 150/300 patients created
  ... 200/300 patients created
  ... 250/300 patients created
  ... 300/300 patients created
✅ Created 300 patients with digital twins
✅ Database seeding completed successfully!
🎉 Ready for demo!
```

---

### 6️⃣ Ejecutar el servidor

```bash
uvicorn app.main:app --reload
```

Verás algo como:

```
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
```

---

## 🎯 Probar el Sistema

### API Docs (Swagger)
Abre en tu navegador:
```
http://localhost:8000/docs
```

Aquí puedes probar todos los endpoints interactivamente.

---

### Frontend 1: Chat "Yo del Futuro"

```
http://localhost:8000/chat-ui
```

**Qué hacer:**
1. Selecciona un paciente del dropdown
2. Escribe: "Hola, ¿por qué debería entrar al programa?"
3. Ve la respuesta empática del "yo del futuro"
4. Continúa la conversación

---

### Frontend 2: Dashboard del Paciente

```
http://localhost:8000/patient-dashboard
```

**Qué hacer:**
1. Selecciona un paciente
2. Revisa su información personal
3. Ve su nivel de riesgo y condiciones
4. Explora sus objetivos de salud con barras de progreso

---

### Frontend 3: Plataforma del Asegurador

```
http://localhost:8000/insurer-platform
```

**Qué hacer:**
1. Se carga automáticamente el resumen poblacional
2. Revisa las métricas principales
3. Analiza la distribución de riesgo
4. Ve el impacto financiero estimado
5. Explora la distribución por programa

---

## 🔧 Troubleshooting

### Error: "OPENAI_API_KEY no está configurada"

**Solución:**
```bash
# Verifica que tu .env tiene la línea:
OPENAI_API_KEY=sk-tu-key-real-aqui

# Reinicia el servidor después de editar .env
```

---

### Error: "could not connect to server: Connection refused"

**Problema:** PostgreSQL no está corriendo.

**Solución:**

**Windows:**
```bash
# Inicia PostgreSQL desde Services o:
pg_ctl -D "C:\Program Files\PostgreSQL\14\data" start
```

**Linux/Mac:**
```bash
sudo service postgresql start
# o
brew services start postgresql@14
```

---

### Error: "relation 'patients' does not exist"

**Problema:** No se crearon las tablas.

**Solución:**
```bash
python db/init_db.py
```

---

### Error: "No module named 'app'"

**Problema:** No estás en el directorio correcto o el venv no está activado.

**Solución:**
```bash
# Asegúrate de estar en la carpeta del proyecto
cd hackaton!

# Activa el entorno virtual
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

---

### Error: "Port 8000 already in use"

**Solución:**
```bash
# Usa otro puerto
uvicorn app.main:app --reload --port 8080

# Luego abre http://localhost:8080/...
```

---

## 📊 Verificar que Todo Funciona

Ejecuta estos comandos para verificar:

```bash
# 1. Verificar que la base de datos tiene datos
# (Deberías ver ~300 filas)
psql -U digital_twin_user -d digital_twin_dev -c "SELECT COUNT(*) FROM patients;"

# 2. Probar el health check
curl http://localhost:8000/health

# Deberías ver:
# {"status":"healthy","app":"Digital Twin Health MVP",...}
```

---

## 🎓 Datos de Prueba

El sistema generó 300 pacientes con distribución realista:

- **~90 pacientes** (30%): Saludables
- **~105 pacientes** (35%): Susceptibles
- **~75 pacientes** (25%): Condición Estable
- **~30 pacientes** (10%): Alta Complejidad

Cada paciente tiene:
- Gemelo digital con nivel de riesgo
- Probabilidad de complicación a 90 días
- Condiciones de salud
- Programas recomendados
- 0-3 objetivos de salud personalizados

---

## 🚀 Siguiente Paso: Desplegar en Render

Cuando estés listo para desplegar en la nube:

1. Sube tu código a GitHub:
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin <tu-repo>
git push -u origin main
```

2. Ve a https://render.com y crea una cuenta

3. Click en "New" → "Blueprint"

4. Conecta tu repositorio de GitHub

5. Render detectará automáticamente `render.yaml` y desplegará todo

6. Agrega tu `OPENAI_API_KEY` en Environment Variables

Ver más detalles en [README.md](README.md#despliegue-en-render)

---

## ✅ Checklist Final

Antes de presentar tu demo, verifica:

- [ ] El servidor corre sin errores
- [ ] Los 3 frontends cargan correctamente
- [ ] El chat responde (verifica tu API key de OpenAI)
- [ ] El dashboard del paciente muestra objetivos
- [ ] La plataforma del asegurador muestra métricas
- [ ] Tienes datos de al menos 300 pacientes
- [ ] Has probado una conversación completa en el chat

---

## 🎉 ¡Listo para Demo!

Ahora tienes un MVP completamente funcional que demuestra:

✅ **Gemelo digital individual** con datos clínicos y comportamentales
✅ **Chat empático** con "yo del futuro" usando IA
✅ **Dashboard personalizado** para pacientes con objetivos
✅ **Vista poblacional** para el asegurador (gemelo poblacional)
✅ **Impacto financiero** simulado a 90 días
✅ **Datos sintéticos** realistas de 300 pacientes

**¡Mucha suerte en tu hackatón!** 🚀

---

## 📞 ¿Necesitas Ayuda?

Si algo no funciona:

1. Revisa la sección Troubleshooting arriba
2. Verifica los logs del servidor
3. Consulta [README.md](README.md) para más detalles
4. Revisa [DATABASE.md](DATABASE.md) para temas de base de datos
