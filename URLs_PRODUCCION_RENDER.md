# 🌐 URLs de Producción - Render
## Plataforma Gemelo Digital en la Nube

**URL Base:** https://digital-twin-health-api.onrender.com

---

## 🎯 Frontends Completos (Lo que funciona en local, ahora en Render)

### 1. Landing Page con Login ⭐ INICIO
```
https://digital-twin-health-api.onrender.com/
```

**Credenciales:**
- Usuario: `admin`
- Contraseña: `hackathon2025`

**Alternativas:**
- `demo` / `2025`
- `colsanitas` / `gemelo2025`

**Qué hace:**
- Pantalla de login con autenticación
- Después del login: 2 tarjetas interactivas
- Click izquierda: Módulo Paciente
- Click derecha: Módulo Administrador

---

### 2. Módulo del Paciente (Plataforma Integrada)
```
https://digital-twin-health-api.onrender.com/plataforma-integrada
```

**Características:**
- ✅ Chat con "yo del futuro" (OpenAI GPT-4)
- ✅ Dashboard familiar (4 perfiles: María, Carlos, Sofía, Abuela Rosa)
- ✅ Gamificación tipo Tamagotchi (puntos, niveles, rachas)
- ✅ 8 hábitos saludables
- ✅ 7 programas de salud (filtrados por edad)
- ✅ Modal de inscripción (18 clínicas en 5 ciudades)
- ✅ Tareas completables (+25 puntos cada una)

**Flujo Demo:**
1. Chat con el "yo del futuro"
2. Ver riesgo cardiovascular (gráfico)
3. Click "Ver mi Gemelo Digital"
4. Seleccionar "Gestor Familiar"
5. Autorizar datos
6. Dashboard de 4 miembros
7. Click en María → Ver su Tamagotchi
8. Marcar hábito (+15 pts)
9. Inscribir en programa (+100 pts)
10. Completar tarea (+25 pts)

---

### 3. Módulo de Administrador (Dashboard Admin)
```
https://digital-twin-health-api.onrender.com/admin-dashboard
```

**Características:**
- ✅ 30 pacientes sintéticos que usaron la plataforma
- ✅ 6 KPIs principales:
  - Total pacientes: 30
  - Enrollment rate: 85%
  - Citas agendadas: 23
  - Salud promedio: 78%
  - Puntos promedio: 1,245
  - Racha promedio: 12 días
- ✅ 4 gráficos interactivos (Chart.js):
  - Distribución por programa (doughnut)
  - Salud por edad (bar)
  - Distribución por ciudad (bar)
  - Horarios más solicitados (horizontal bar)
- ✅ Filtros (búsqueda, programa, ciudad)
- ✅ Exportar a CSV

**Datos mostrados:**
- DNI, Nombre, Edad, Ciudad, Programa
- Estado de inscripción
- Cita agendada (clínica + horario)
- Salud, Puntos, Nivel, Racha
- Última actividad

---

## 📡 API REST Endpoints

### Health Check
```
https://digital-twin-health-api.onrender.com/health
```
Responde:
```json
{
  "status": "healthy",
  "app": "Digital Twin Health MVP",
  "version": "1.0.0",
  "openai_configured": true
}
```

---

### Documentación Interactiva
```
https://digital-twin-health-api.onrender.com/docs
```
Swagger UI con todos los endpoints documentados

---

### Listar Pacientes (300)
```
https://digital-twin-health-api.onrender.com/patients/
```
Retorna array con 300 pacientes de la base de datos PostgreSQL

---

### Resumen Poblacional
```
https://digital-twin-health-api.onrender.com/analytics/population-summary
```
Retorna:
```json
{
  "total_patients": 300,
  "enrollment_rate": 71.0,
  "enrolled_in_programs": 213,
  "program_distribution": {
    "DIABETES": 112,
    "OBESITY": 102,
    "HYPERTENSION": 63,
    "CARDIOVASCULAR": 50,
    "PRENATAL": 52
  }
}
```

---

### Paciente Individual
```
https://digital-twin-health-api.onrender.com/patients/{id}
```
Ejemplo: `/patients/1`

---

### Crear Sesión de Chat
```
POST https://digital-twin-health-api.onrender.com/chat/session
```
Body:
```json
{
  "patient_id": 1
}
```

---

### Enviar Mensaje al Chat
```
POST https://digital-twin-health-api.onrender.com/chat/message
```
Body:
```json
{
  "session_id": 1,
  "message": "Hola, ¿por qué debería entrar al programa?"
}
```

Responde con mensaje del "yo del futuro"

---

## 🎤 Script de Presentación para Hackathon

### Opción 1: Solo Frontends (5 minutos)

**MINUTO 0-1: Login y Landing**
> "Nuestra plataforma tiene autenticación. Las credenciales están en pantalla."
>
> [Abrir: https://digital-twin-health-api.onrender.com/]
>
> [Login: admin / hackathon2025]
>
> "Ahora vemos las 2 opciones: Módulo Paciente y Módulo Administrador."

**MINUTO 1-3: Módulo Paciente**
> "Empecemos con el paciente."
>
> [Click en tarjeta del paciente]
>
> "Chat con IA que simula 'yo del futuro' para motivar enrollment."
>
> [Mostrar chat → Gráfico de riesgo]
>
> "Dashboard familiar tipo Tamagotchi. Gamificación con puntos."
>
> [Mostrar 4 perfiles → Click en María]
>
> "Marcar hábito: +15 puntos. Inscribir programa: +100 puntos. Completar tarea: +25 puntos."

**MINUTO 3-5: Módulo Admin**
> "Ahora veamos qué ve el asegurador."
>
> [Volver → Click en tarjeta admin]
>
> "30 pacientes que usaron la plataforma. KPIs: 85% enrollment."
>
> [Mostrar gráficos]
>
> "Podemos ver quién agendó cita, en qué clínica, qué horario."
>
> [Filtrar por programa]
>
> "Y exportar todo a CSV para análisis."

---

### Opción 2: API + Frontends (7 minutos)

**MINUTO 0-2: API REST**
> "Backend desplegado en Render con PostgreSQL."
>
> [Abrir: https://digital-twin-health-api.onrender.com/docs]
>
> "API REST con 8 endpoints documentados."
>
> [Click en GET /analytics/population-summary → Try it out → Execute]
>
> "300 pacientes sintéticos. 71% enrollment rate. 213 inscritos."

**MINUTO 2-7: Frontends**
> [Seguir script de Opción 1]

---

## 🔧 Troubleshooting

### Problema: "Page not loading" en Render

**Causa:** Render puede tardar 30-60 segundos en despertar (plan Free)

**Solución:**
- Espera 1 minuto
- Refresca la página (F5)
- Si persiste, visita `/health` primero para despertar el servicio

---

### Problema: "Chat no funciona"

**Causa:** API key de OpenAI no configurada o inválida

**Verificar:**
```
https://digital-twin-health-api.onrender.com/health
```

Si `"openai_configured": false`, la API key no está configurada.

**Solución:**
1. Ir a Render Dashboard
2. Environment → OPENAI_API_KEY
3. Verificar que existe y es correcta
4. Redeploy

---

### Problema: "No veo datos en Admin Dashboard"

**Causa:** Admin dashboard usa datos hardcodeados (30 pacientes en el HTML)

**Solución:** No requiere solución. Los 30 pacientes son datos de ejemplo en el frontend. NO vienen de la base de datos.

---

## 📊 Comparación: Local vs Render

| Característica | Local (BAT files) | Render (Producción) |
|---------------|-------------------|---------------------|
| **Landing con Login** | ✅ ABRIR_PLATAFORMA.bat | ✅ https://.../  |
| **Módulo Paciente** | ✅ plataforma_integrada.html | ✅ https://.../plataforma-integrada |
| **Módulo Admin** | ✅ admin_dashboard.html | ✅ https://.../admin-dashboard |
| **API REST** | ✅ localhost:8000 | ✅ https://.../ |
| **Base de Datos** | ✅ PostgreSQL local | ✅ PostgreSQL Render |
| **Internet requerido** | ❌ No | ✅ Sí |
| **Acceso público** | ❌ Solo local | ✅ Cualquiera con URL |

---

## 🎯 Checklist Pre-Presentación

Antes de la demo del hackathon:

- [ ] Visitar `/` y verificar login funciona
- [ ] Login con admin/hackathon2025
- [ ] Verificar que aparecen las 2 tarjetas
- [ ] Click en módulo paciente → Verifica que carga
- [ ] Volver y click en módulo admin → Verifica que carga
- [ ] Verificar `/health` responde healthy
- [ ] Verificar `/docs` muestra documentación
- [ ] Anotar URL en papel/celular para compartir

---

## 💡 Tips para la Presentación

1. **Abre las URLs 5 minutos antes** (para despertar el servicio Free)
2. **Ten las credenciales a mano:** admin / hackathon2025
3. **Practica el flujo completo** al menos 1 vez
4. **Ten backup:** Si falla internet, usa los BAT files locales
5. **Menciona GitHub:** El código está público y documentado

---

## 📦 Recursos Adicionales

**GitHub:**
```
https://github.com/and5256841/hackaton-keralty
```

**Documentación Local:**
- `CREDENCIALES_ACCESO.md` - Guía de login
- `LANDING_PAGE_GUIA.md` - Guía de landing page
- `DASHBOARD_ADMIN_GUIA.md` - Guía de módulo admin
- `DEPLOY_RENDER_GUIA.md` - Guía de despliegue

---

## ✅ Estado Final

- 🟢 **Backend API:** Funcionando con 300 pacientes
- 🟢 **Landing Page:** Con login funcional
- 🟢 **Módulo Paciente:** Gamificación completa
- 🟢 **Módulo Admin:** 30 pacientes, KPIs, gráficos
- 🟢 **Base de Datos:** PostgreSQL con datos sintéticos
- 🟢 **Documentación:** Completa y accesible

---

**¡LISTO PARA EL HACKATHON!** 🚀

**Fecha:** 20 de Noviembre 2025
**Plataforma:** Render (plan Free)
**Tiempo de deploy:** 3-5 minutos
**Uptime:** 24/7 (con cold start de 30-60s en inactividad)
