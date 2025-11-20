# 🚀 Guía de Despliegue en Render
## Plataforma Gemelo Digital - Hackathon 2025

---

## 📋 Prerrequisitos

Antes de comenzar, asegúrate de tener:

1. ✅ Cuenta en GitHub (ya creada: https://github.com/and5256841/hackaton-keralty)
2. ✅ Código subido a GitHub (completado)
3. ⚠️ **API Key de OpenAI** - Necesitarás configurarla en Render
4. 🆕 Cuenta en Render (si no tienes, crear en https://render.com)

---

## 🔐 Obtener tu API Key de OpenAI

### Paso 1: Ir a OpenAI Platform
Visita: https://platform.openai.com/api-keys

### Paso 2: Iniciar sesión
- Usa tu cuenta de OpenAI
- Si no tienes cuenta, créala primero

### Paso 3: Crear nueva API Key
1. Click en **"Create new secret key"**
2. Dale un nombre: `Render - Hackathon Keralty`
3. Click en **"Create secret key"**
4. **IMPORTANTE:** Copia la key inmediatamente (solo se muestra una vez)
5. Guárdala en un lugar seguro (la necesitarás en el Paso 5 de Render)

**Formato de la key:**
```
sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
```

**⚠️ Nunca compartas esta key públicamente**

---

## 🌐 Despliegue en Render

### Paso 1: Crear cuenta en Render

1. Ve a https://render.com
2. Click en **"Get Started"**
3. Opción recomendada: **"Sign up with GitHub"**
   - Esto conecta automáticamente tu cuenta de GitHub
4. Autoriza a Render para acceder a tus repositorios

---

### Paso 2: Conectar el Repositorio

1. En el Dashboard de Render, click en **"New +"** (esquina superior derecha)
2. Selecciona **"Blueprint"**
3. Te pedirá conectar un repositorio
4. Busca: `and5256841/hackaton-keralty`
5. Click en **"Connect"**

**¿Por qué Blueprint?**
- Render detectará automáticamente el archivo `render.yaml`
- Creará tanto el servicio web como la base de datos PostgreSQL
- Configurará las variables de entorno automáticamente

---

### Paso 3: Revisar Configuración del Blueprint

Render mostrará la configuración detectada:

**Web Service:**
- **Name:** digital-twin-health-api
- **Environment:** Docker
- **Plan:** Free
- **Region:** Oregon (US West)

**Database:**
- **Name:** digital-twin-db
- **Type:** PostgreSQL 15
- **Plan:** Free
- **Database Name:** digital_twin_production
- **User:** digital_twin_user

Click en **"Apply"** para continuar

---

### Paso 4: Esperar Creación de Recursos

Render comenzará a crear:

1. **Base de datos PostgreSQL** (1-2 minutos)
   - Estado: Creating → Available

2. **Web Service** (3-5 minutos)
   - Clonando repositorio
   - Building Docker image
   - Deploying

**Puedes ver los logs en tiempo real**

---

### Paso 5: Configurar OPENAI_API_KEY ⚠️ IMPORTANTE

Una vez que el servicio esté creado:

1. Ve a tu servicio `digital-twin-health-api`
2. Click en la pestaña **"Environment"** (menú izquierdo)
3. Busca la variable `OPENAI_API_KEY`
4. Verás que dice `sync: false` (no se configuró automáticamente)
5. Click en **"Edit"** o **"Add Environment Variable"**
6. Completa:
   - **Key:** `OPENAI_API_KEY`
   - **Value:** (pega tu API key de OpenAI aquí)
   ```
   sk-proj-XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
   ```
7. Click en **"Save Changes"**

**Render redesplegará automáticamente** (2-3 minutos)

---

### Paso 6: Verificar Variables de Entorno

Asegúrate de que estén configuradas:

| Variable | Valor | Fuente |
|----------|-------|--------|
| **OPENAI_API_KEY** | sk-proj-XXXXX... | Manual (Paso 5) |
| **OPENAI_MODEL** | gpt-4-turbo-preview | render.yaml |
| **DATABASE_URL** | postgres://... | Automática (de la DB) |
| **ANALYTICS_DATABASE_URL** | postgres://... | Automática (de la DB) |
| **APP_NAME** | Digital Twin Health MVP | render.yaml |
| **DEBUG** | false | render.yaml |

---

### Paso 7: Inicializar la Base de Datos

Una vez que el servicio esté **Live** (verde):

#### Opción A: Desde la Shell de Render (Recomendado)

1. En tu servicio `digital-twin-health-api`
2. Click en **"Shell"** (menú izquierdo)
3. Esto abre una terminal dentro del contenedor
4. Ejecuta los siguientes comandos:

```bash
# Crear las tablas
python db/init_db.py

# Generar 300 pacientes sintéticos
python db/seed_synthetic_data.py
```

5. Deberías ver:
```
✅ Database initialized successfully
✅ Created 300 patients
✅ Created 600 digital twins
✅ Created 450 health goals
```

#### Opción B: Desde SSH (Avanzado)

Si prefieres SSH:
```bash
# Obtener el comando SSH desde Render Dashboard
# Ejemplo:
ssh srv-XXXXXXXXXX@ssh.oregon.render.com

# Luego ejecutar los mismos comandos
python db/init_db.py
python db/seed_synthetic_data.py
```

---

### Paso 8: Verificar el Health Check

1. Render mostrará la URL de tu servicio:
   ```
   https://digital-twin-health-api.onrender.com
   ```

2. Visita:
   ```
   https://digital-twin-health-api.onrender.com/health
   ```

3. Deberías ver:
   ```json
   {
     "status": "healthy",
     "service": "Digital Twin Health MVP",
     "version": "1.0.0"
   }
   ```

---

### Paso 9: Probar la Documentación Interactiva

Visita:
```
https://digital-twin-health-api.onrender.com/docs
```

Deberías ver la documentación de FastAPI con todos los endpoints:

- `GET /health` - Health check
- `GET /patients/` - Listar pacientes
- `POST /chat/session` - Crear sesión de chat
- `POST /chat/message` - Enviar mensaje al chat
- `GET /analytics/population-summary` - Resumen poblacional

---

### Paso 10: Probar los Frontends

#### Chat del Paciente
```
https://digital-twin-health-api.onrender.com/chat-ui
```

#### Dashboard del Paciente
```
https://digital-twin-health-api.onrender.com/patient-dashboard
```

#### Dashboard del Asegurador
```
https://digital-twin-health-api.onrender.com/insurer-platform
```

**NOTA:** Los frontends HTML standalone (index.html, plataforma_integrada.html, admin_dashboard.html) NO requieren el backend de Render. Solo los frontends del backend (chat.html, patient_dashboard.html, insurer_platform.html) necesitan Render.

---

## 🔧 Troubleshooting

### Problema 1: Build Failed

**Síntomas:**
- Render muestra "Build failed"
- Logs muestran errores de Docker

**Soluciones:**

1. Verifica que el Dockerfile esté en el repositorio:
   ```bash
   git ls-files | grep Dockerfile
   ```

2. Verifica que requirements.txt sea correcto:
   ```bash
   cat requirements.txt
   ```

3. Re-trigger deploy:
   - Render Dashboard → Manual Deploy → "Clear build cache & deploy"

---

### Problema 2: Health Check Failing

**Síntomas:**
- Servicio muestra "Unhealthy"
- No responde en `/health`

**Soluciones:**

1. Revisa los logs:
   - Render Dashboard → Logs
   - Busca errores de inicio

2. Verifica variables de entorno:
   - Especialmente `DATABASE_URL`
   - Debe empezar con `postgresql://`

3. Verifica que el puerto sea correcto:
   - Render usa la variable `PORT` automáticamente
   - FastAPI debe escuchar en `0.0.0.0:$PORT`

---

### Problema 3: Error de OpenAI API

**Síntomas:**
```
Error: Incorrect API key provided
```

**Soluciones:**

1. Verifica que configuraste `OPENAI_API_KEY` en Render
2. La key debe empezar con `sk-proj-` o `sk-`
3. No debe tener espacios ni caracteres extra
4. Crea una nueva key en OpenAI Platform si la anterior no funciona

---

### Problema 4: Base de Datos Vacía

**Síntomas:**
- Endpoints retornan arrays vacíos
- Chat no encuentra pacientes

**Solución:**

Inicializar la base de datos manualmente:

```bash
# Desde Render Shell
python db/init_db.py
python db/seed_synthetic_data.py
```

---

### Problema 5: "Free instance will spin down with inactivity"

**Síntoma:**
- Mensaje en Render Dashboard

**Explicación:**
- El plan Free de Render apaga el servicio después de 15 minutos de inactividad
- La primera petición después de estar inactivo tarda 30-60 segundos (cold start)
- Esto es normal y esperado en el plan gratuito

**Soluciones:**

1. **Para demos:** Haz una petición 2-3 minutos antes de presentar
2. **Para producción:** Upgrade a plan Starter ($7/mes) que nunca se apaga

---

## 📊 Monitoreo y Logs

### Ver Logs en Tiempo Real

1. Render Dashboard → Tu servicio
2. Click en **"Logs"** (menú izquierdo)
3. Verás logs de:
   - Requests HTTP
   - Errores de la aplicación
   - Queries a la base de datos

### Métricas

Render muestra automáticamente:
- **CPU Usage**
- **Memory Usage**
- **Request Count**
- **Response Time**

---

## 💰 Costos

### Plan Free de Render:

**Web Services:**
- ✅ Gratis
- ⚠️ Se apaga después de 15 min de inactividad
- ⚠️ 750 horas/mes (suficiente para hackathon)

**PostgreSQL:**
- ✅ Gratis
- ⚠️ 90 días de retención de backups
- ⚠️ 1 GB de almacenamiento

**Costo total del hackathon: $0**

---

## 🔒 Seguridad

### Buenas Prácticas Implementadas:

✅ **API Key en variables de entorno**
- No está hardcodeada en el código
- Solo visible en Render Dashboard

✅ **HTTPS automático**
- Render provee certificado SSL gratis
- Todas las URLs son `https://`

✅ **Secrets management**
- Variables de entorno encriptadas
- No se muestran en logs

✅ **Database credentials**
- Generadas automáticamente por Render
- Rotadas periódicamente

---

## 🎯 Checklist Final

Antes de la demo del hackathon:

- [ ] Repositorio en GitHub actualizado
- [ ] Servicio en Render con estado "Live" (verde)
- [ ] OPENAI_API_KEY configurada correctamente
- [ ] Base de datos inicializada (300 pacientes)
- [ ] Health check responde correctamente
- [ ] Documentación (/docs) carga correctamente
- [ ] Al menos 1 endpoint de chat funciona
- [ ] URL pública anotada y lista para compartir

---

## 📝 URLs Finales

**API Backend:**
```
https://digital-twin-health-api.onrender.com
```

**Documentación Interactiva:**
```
https://digital-twin-health-api.onrender.com/docs
```

**Health Check:**
```
https://digital-twin-health-api.onrender.com/health
```

**Chat Frontend:**
```
https://digital-twin-health-api.onrender.com/chat-ui
```

**Guarda estas URLs** para compartir con jueces/stakeholders del hackathon.

---

## 🎤 Script para Demo con Render

**Durante la presentación del hackathon:**

> "Nuestra plataforma está desplegada en producción en Render. Déjenme mostrarles."
>
> [Abrir: https://digital-twin-health-api.onrender.com/docs]
>
> "Aquí tenemos nuestra API REST con 8 endpoints documentados. Voy a probar el chat con IA."
>
> [Ir a POST /chat/message → Try it out]
>
> "Creo una sesión de chat para el paciente 1..."
>
> [Ejecutar y mostrar respuesta del 'yo del futuro']
>
> "Como pueden ver, la IA responde de manera empática y motivacional. Todo esto está funcionando en la nube, sin necesidad de instalación."

---

## 🆘 Soporte Durante el Hackathon

Si encuentras problemas durante el evento:

1. **Revisa los logs en Render Dashboard**
2. **Verifica el health check:** `/health`
3. **Comprueba variables de entorno**
4. **Re-deploy manual** (botón "Manual Deploy" en Render)

**Tiempo estimado de re-deploy:** 3-5 minutos

---

## ✅ Resumen

**Has completado:**

1. ✅ Código en GitHub sin API keys expuestas
2. ✅ Configuración automática con render.yaml
3. ✅ Instrucciones para configurar OPENAI_API_KEY
4. ✅ Guía para inicializar base de datos
5. ✅ URLs listas para compartir

**Próximo paso:** Configurar el despliegue en Render siguiendo esta guía.

---

**VERSIÓN:** 1.0 - Guía de Despliegue en Render
**FECHA:** 19 de Noviembre 2025
**REPOSITORIO:** https://github.com/and5256841/hackaton-keralty

---

*Plataforma Gemelo Digital - Hackathon 2025*
*Listo para producción en la nube*
