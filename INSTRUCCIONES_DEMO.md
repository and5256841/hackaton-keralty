# 🏥 Plataforma Gemelo Digital - Demo Hackathon

## 🆕 VERSIÓN MEJORADA - Sin Bucles + OpenAI Real

### ✅ Mejoras Implementadas:
- ❌➡️✅ **Bucle infinito eliminado** - Conversación controlada
- 🤖 **OpenAI GPT-4 integrado** - Respuestas naturales y contextuales
- 💬 **Manejo de objeciones** - Responde a "no tengo tiempo", "es caro", etc.
- 🎯 **Call-to-action dinámico** - Transición natural después de 3 intercambios

---

## 🚀 Inicio Rápido

### ⚠️ PASO 1: Verificar OpenAI API (RECOMENDADO)
Antes de la demo, verifica que tu API funciona:

**Doble clic en:** `PROBAR_OPENAI.bat`

- ✅ Mensaje verde → Todo listo para la demo
- ❌ Mensaje rojo → Revisa créditos en [platform.openai.com](https://platform.openai.com)

### PASO 2: Abrir la Plataforma

#### Opción A: Doble clic (Recomendado)
Haz **doble clic** en `ABRIR_PLATAFORMA.bat`

#### Opción B: Abrir manualmente
Abre `frontend\plataforma_final.html` en tu navegador

---

## 📋 Flujo de la Demo

### 1️⃣ Pantalla de Selección de Pacientes
- Verás 4 pacientes de ejemplo con diferentes niveles de riesgo
- Cada tarjeta muestra:
  - Nombre y avatar
  - Edad y ciudad
  - Condiciones médicas
  - Nivel de riesgo (bajo/medio/alto)

**Pacientes disponibles:**
- **María González** (45 años, Bogotá) - Riesgo ALTO
  - Hipertensión, Diabetes Tipo 2, Obesidad
  - TFG: 55 ml/min
  - Riesgo cardiovascular: 35%

- **Juan Pérez** (38 años, Medellín) - Riesgo MEDIO
  - Prediabetes, Sobrepeso
  - TFG: 85 ml/min
  - Riesgo cardiovascular: 15%

- **Ana Martínez** (52 años, Cali) - Riesgo ALTO
  - Enfermedad Renal Crónica, Hipertensión
  - TFG: 42 ml/min
  - Riesgo cardiovascular: 40%

- **Carlos Rodríguez** (29 años, Barranquilla) - Riesgo BAJO
  - Saludable (control preventivo)
  - TFG: 110 ml/min
  - Riesgo cardiovascular: 5%

### 2️⃣ Chat con "Yo del Futuro"
Después de seleccionar un paciente, verás una conversación estilo WhatsApp donde:

**Mensajes automáticos iniciales (3-4 mensajes):**
1. Saludo personalizado del "yo del futuro" (15 años mayor)
2. Datos específicos del paciente (edad, ciudad, condiciones)
3. **Gráfico cardiovascular embebido** mostrando:
   - Riesgo actual
   - Riesgo en 5 años SIN programa
   - Riesgo en 5 años CON programa
4. Mención de TFG (Tasa de Filtración Glomerular)
5. Mensaje dramático y persuasivo basado en el nivel de riesgo
6. **Referencia bibliográfica** (National Kidney Foundation)

**Tono del chat:**
- **Riesgo Alto**: Mensajes muy dramáticos y urgentes
- **Riesgo Medio**: Mensajes preventivos y motivadores
- **Riesgo Bajo**: Mensajes de felicitación y prevención

**Interacción:**
- Escribe cualquier mensaje para responder
- El "yo del futuro" recomienda programas específicos
- Haz clic en "Ver Mi Gemelo Digital" para continuar

### 3️⃣ Gemelo Digital Interactivo
Esta pantalla muestra el gemelo digital del paciente con:

**Avatar Interactivo:**
- Monigote/avatar con indicadores de salud
- 3 indicadores con flechas:
  - ❤️ Salud Cardiovascular
  - 🔵 Función Renal
  - 🫁 Función Respiratoria

**Métricas Actuales:**
- Nivel de riesgo
- Condiciones detectadas
- TFG actual
- Riesgo cardiovascular

**Programas Recomendados:**
Lista de 37+ programas de salud organizados por:
- Ciudad (Bogotá, Medellín, Cali, Barranquilla)
- Centro médico georeferenciado
- Tipo de programa (cardio, renal, diabetes, etc.)

**Timeline Longitudinal:**
Visualización de la evolución de salud:
- **HOY**: Estado actual
- **+3 MESES**: Mejora esperada con programa
- **+1 AÑO**: Meta de salud

**Acciones disponibles:**
- 📅 Agendar Cita
- 📊 Ver Panel del Asegurador

### 4️⃣ Panel del Asegurador
Vista administrativa para configurar la estrategia de contacto:

**Métricas Poblacionales:**
- Total de pacientes
- Distribución por nivel de riesgo
- Pacientes con programas recomendados
- Engagement promedio

**Configuración de Cadencia:**
6 opciones configurables:
1. **Frecuencia de WhatsApp**: Diario, Semanal, Quincenal, Mensual
2. **Llamadas Telefónicas**: Nunca, Mensual, Trimestral
3. **Recordatorios de Citas**: Sí/No
4. **Mensajes de Cumpleaños**: Sí/No
5. **Encuestas de Salud**: Nunca, Mensual, Trimestral
6. **Alertas de Riesgo Alto**: Sí/No

**Funcionalidad:**
- Botón "Guardar Configuración" (simulado)
- Posibilidad de descargar datos a Excel/CSV

---

## 🎯 Puntos Clave de la Demo

### Innovación Tecnológica
1. **Conversación Personalizada con IA**: Usa datos específicos del paciente
2. **Visualización de Datos**: Gráficos embebidos en el chat (Chart.js)
3. **Gemelo Digital Interactivo**: Avatar con indicadores visuales
4. **Timeline Longitudinal**: Proyección de salud a futuro
5. **Geolocalización**: Programas mapeados por ciudad

### Impacto en el Negocio
- **Aumenta enrollment** en programas de salud
- **Reduce costos** de complicaciones (mostrado en gráficos)
- **Mejora engagement** con mensajería personalizada
- **Prevención proactiva** basada en riesgo

### Experiencia de Usuario
- **Familiar**: Diseño estilo WhatsApp
- **Emocional**: "Yo del futuro" genera conexión
- **Educativo**: Referencias bibliográficas y datos médicos
- **Actionable**: Llamados a la acción claros

---

## 🔧 Información Técnica

### Stack Tecnológico
**Frontend (Todo en un archivo HTML):**
- HTML5 + CSS3
- JavaScript Vanilla
- Chart.js 4.4.0 (CDN)
- Diseño responsive

**Backend (Disponible pero no requerido para demo):**
- FastAPI 0.109.0
- SQLite database
- 300 pacientes sintéticos
- OpenAI GPT-4 integration

### API de OpenAI
La plataforma está configurada para usar OpenAI GPT-4, pero para la demo:
- Los mensajes son **simulados** (no requiere API key activa)
- Respuestas pre-programadas basadas en riesgo del paciente
- Para activar IA real: configurar `OPENAI_API_KEY` en `.env`

### Base de Datos
- 300 pacientes sintéticos generados con Faker
- Distribución realista:
  - 30% saludables
  - 35% susceptibles
  - 25% estables con condiciones
  - 10% alta complejidad

---

## 🎤 Script Sugerido para Presentación

### Apertura (30 segundos)
> "Hoy les presentamos una solución innovadora para aumentar el enrollment en programas de salud: una plataforma de gemelo digital que conecta a los pacientes con su 'yo del futuro' a través de conversaciones personalizadas impulsadas por IA."

### Demo Pantalla 1 (30 segundos)
> "Comenzamos seleccionando un paciente. Vamos a elegir a María González, de 45 años, con alto riesgo cardiovascular y renal. Observen cómo el sistema ya identifica sus condiciones y nivel de riesgo."

### Demo Pantalla 2 (1 minuto)
> "Ahora María recibe mensajes de su 'yo del futuro', 15 años mayor. Observen cómo la conversación incluye datos médicos específicos: su TFG de 55 ml/min indica enfermedad renal crónica estadio 3. El gráfico muestra que sin intervención, su riesgo cardiovascular aumentaría del 35% al 50% en 5 años. Pero con el programa, podría reducirse al 25%."

### Demo Pantalla 3 (45 segundos)
> "En el gemelo digital vemos indicadores visuales de su salud actual y una timeline que muestra la mejora esperada en 3 meses y 1 año. Los programas recomendados están georreferenciados a su ciudad, Bogotá, en centros médicos específicos."

### Demo Pantalla 4 (30 segundos)
> "Finalmente, el asegurador puede configurar la cadencia de contacto: WhatsApp semanal, llamadas mensuales, recordatorios automáticos. Todo optimizado según el nivel de riesgo del paciente."

### Cierre (30 segundos)
> "Esta solución combina storytelling emocional, datos médicos rigurosos y tecnología de IA para transformar el engagement del paciente. El resultado: más enrollment, menos complicaciones, y mejor salud poblacional."

---

## 📊 Datos de Impacto

### Métricas Simuladas
- **300 pacientes** en base de datos
- **37+ programas** de salud disponibles
- **4 ciudades** con geolocalización
- **Reducción estimada del 40%** en riesgo cardiovascular con programas

### Referencias Médicas
- National Kidney Foundation (2023)
- TFG < 60 ml/min = Enfermedad Renal Crónica Estadio 3
- Riesgo cardiovascular proyectado a 10 años (Framingham Score)

---

## ✅ Checklist de Demo

Antes de presentar, verifica:
- [ ] El archivo `plataforma_final.html` abre correctamente
- [ ] Los 4 pacientes se muestran en la pantalla inicial
- [ ] El chat genera mensajes automáticos al seleccionar paciente
- [ ] El gráfico cardiovascular se renderiza correctamente
- [ ] El timeline muestra las 3 etapas
- [ ] La configuración de cadencia es interactiva

---

## 🆘 Solución de Problemas

### El gráfico no se muestra
- Verifica conexión a internet (Chart.js se carga desde CDN)
- Abre la consola del navegador (F12) y busca errores

### Los emojis no se ven
- Usa un navegador moderno (Chrome, Edge, Firefox)
- Los emojis son parte del diseño visual

### Quiero activar la IA real de OpenAI
1. Edita el archivo `.env`
2. Agrega tu API key: `OPENAI_API_KEY=tu-clave-aqui`
3. Inicia el servidor: `python -m uvicorn app.main:app`
4. Modifica el código JavaScript para hacer llamadas al backend

---

## 🏆 Ventajas Competitivas

1. **Único en su tipo**: No hay soluciones que combinen gemelo digital + "yo del futuro"
2. **Evidencia médica**: Referencias bibliográficas integradas
3. **Personalización extrema**: Datos específicos del paciente en cada mensaje
4. **ROI medible**: Gráficos que muestran reducción de costos
5. **Escalable**: De 300 a 300,000 pacientes con la misma arquitectura

---

## 📞 Contacto y Créditos

**Desarrollado para:** Hackathon de Innovación en Salud
**Tecnología:** FastAPI + OpenAI GPT-4 + Chart.js
**Demo:** Completamente funcional sin backend (simulado)

---

¡Buena suerte en el hackathon! 🚀
