# 📊 FLUJO VISUAL COMPLETO
## Diagrama de Usuario - Plataforma Integrada

---

## 🎯 JOURNEY MAP COMPLETO

```
┌─────────────────────────────────────────────────────────────────────┐
│                      INICIO - LANDING PAGE                          │
│                                                                      │
│  👤 Usuario entra a la plataforma                                   │
│      ↓                                                               │
│  🔹 Se carga automáticamente PANTALLA 1: Chat WhatsApp             │
└─────────────────────────────────────────────────────────────────────┘
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│                  PANTALLA 1: CHAT WHATSAPP                          │
│                  Conversación con "Yo del Futuro"                   │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  🤖 MENSAJE 1 (Auto, 0.5s):                                         │
│     "Hola [Nombre], soy TÚ pero del futuro..."                     │
│                                                                      │
│  🤖 MENSAJE 2 (Auto, 4s):                                           │
│     "Tengo que contarte algo urgente sobre tu salud..."            │
│     📊 GRÁFICO DE RIESGO CARDIOVASCULAR                            │
│                                                                      │
│  🤖 MENSAJE 3 (Auto, 8s):                                           │
│     "Mira esta cita médica que tuve..."                            │
│     🎫 IMAGEN DE CITA FUTURISTA CON QR                             │
│                                                                      │
│  🤖 MENSAJE 4 (Auto, 12s):                                          │
│     "¿Qué te preocupa más de tu salud en este momento?"            │
│                                                                      │
│  👤 USUARIO ESCRIBE → OpenAI GPT-4 responde                        │
│                                                                      │
│  🔄 CONVERSACIÓN INTERACTIVA (2-3 intercambios)                    │
│     ├─ Manejo de objeciones                                        │
│     ├─ Empatía y urgencia personalizada                            │
│     └─ Motivación para enrollment                                  │
│                                                                      │
│  ⬇️ DESPUÉS DE 3 MENSAJES DEL USUARIO                              │
│                                                                      │
│  🔘 BOTÓN APARECE: "Ver mi Gemelo Digital 🔮"                      │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
                        [USUARIO HACE CLICK]
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│                  PANTALLA 2: SELECCIÓN DE ROL                       │
│                  ¿Individual o Gestor Familiar?                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌─────────────────────────┐    ┌─────────────────────────┐       │
│  │   👤 INDIVIDUAL          │    │   👨‍👩‍👧‍👦 GESTOR FAMILIAR  │       │
│  │                          │    │                          │       │
│  │  Solo mi salud           │    │  Familia completa        │       │
│  │  Datos propios           │    │  Menores + Ancianos      │       │
│  │  Vista simple            │    │  4 perfiles              │       │
│  │                          │    │  Requiere autorización   │       │
│  │  [Continuar]             │    │  [Continuar]             │       │
│  └─────────────────────────┘    └─────────────────────────┘       │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                   ↓                              ↓
           [INDIVIDUAL]                    [GESTOR FAMILIAR]
                   ↓                              ↓
            (Saltar P3)                           ↓
                   ↓
                   └────────────────┐             ↓
                                    ↓             ↓

┌─────────────────────────────────────────────────────────────────────┐
│         PANTALLA 3: AUTORIZACIÓN DE DATOS SENSIBLES                 │
│         (Solo si eligió "Gestor Familiar")                          │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  📜 CONSENTIMIENTO INFORMADO                                        │
│                                                                      │
│  ☐ Autorización legal para gestionar datos de menores/ancianos     │
│  ☐ Compromiso de confidencialidad médica                           │
│  ☐ Aceptación de términos y condiciones                            │
│                                                                      │
│  ⚠️ Los 3 checkboxes deben estar marcados                          │
│                                                                      │
│  🔘 [Continuar] (deshabilitado hasta marcar todos)                 │
│                                                                      │
│  📋 Cumplimiento: HIPAA, GDPR, Ley 1581 de 2012                    │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
                    [USUARIO ACEPTA TODO]
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│              PANTALLA 4: DASHBOARD FAMILIAR                         │
│              Vista de 4 Miembros de la Familia                      │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────┐  ┌──────────────────┐                        │
│  │ 👩 MARÍA         │  │ 👨 CARLOS        │                        │
│  │ Titular, 45 años │  │ Esposo, 48 años  │                        │
│  │                  │  │                  │                        │
│  │ 🟡 Salud: 65%    │  │ 🟢 Salud: 80%    │                        │
│  │ ⭐ 850 pts       │  │ ⭐ 1,240 pts     │                        │
│  │ 🏆 Nivel 3       │  │ 🏆 Nivel 4       │                        │
│  │ 🔥 Racha: 7d     │  │ 🔥 Racha: 14d    │                        │
│  │                  │  │                  │                        │
│  │ 💊 🏃 🥗 💧      │  │ 💊 🏃 🥗 💧      │                        │
│  │                  │  │                  │                        │
│  │ [Ver Tamagotchi] │  │ [Ver Tamagotchi] │                        │
│  └──────────────────┘  └──────────────────┘                        │
│                                                                      │
│  ┌──────────────────┐  ┌──────────────────┐                        │
│  │ 👧 SOFÍA         │  │ 👵 ABUELA ROSA   │                        │
│  │ Hija, 12 años    │  │ Madre, 78 años   │                        │
│  │                  │  │                  │                        │
│  │ 🟢 Salud: 95%    │  │ 🟡 Salud: 70%    │                        │
│  │ ⭐ 1,850 pts     │  │ ⭐ 620 pts       │                        │
│  │ 🏆 Nivel 5       │  │ 🏆 Nivel 2       │                        │
│  │ 🔥 Racha: 21d ⭐  │  │ 🔥 Racha: 5d     │                        │
│  │                  │  │                  │                        │
│  │ 💊 🏃 🥗 💧      │  │ 💊 🏃 🥗 💧      │                        │
│  │                  │  │                  │                        │
│  │ [Ver Tamagotchi] │  │ [Ver Tamagotchi] │                        │
│  └──────────────────┘  └──────────────────┘                        │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
                   [CLICK EN CUALQUIER TARJETA]
                              ↓
                       (Ejemplo: María)
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│          PANTALLA 5: TAMAGOTCHI DETALLADO - MARÍA                   │
│          Vista Completa con Todas las Secciones                     │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 🔙 Volver al Dashboard                                        │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ╔══════════════════════════════════════════════════════════════╗  │
│  ║              👩 AVATAR GIGANTE (Flotando)                    ║  │
│  ║                                                               ║  │
│  ║  MARÍA GONZÁLEZ - 45 años - Bogotá                           ║  │
│  ║  Estado: 😐 Neutral                                           ║  │
│  ║                                                               ║  │
│  ║  ████████████░░░░░ 65% Salud                                 ║  │
│  ║  ⭐ 850 puntos | 🏆 Nivel 3 | 🔥 7 días                      ║  │
│  ╚══════════════════════════════════════════════════════════════╝  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 🌟 HÁBITOS SALUDABLES                                         │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                               │  │
│  │  ☐ 🚭 No consumo de tabaco                        +15 pts    │  │
│  │  ☐ 🍷 Consumo responsable de alcohol              +15 pts    │  │
│  │  ☐ 🧘 Prevención de burnout                        +15 pts    │  │
│  │  ☐ 🏃 Actividad física regular                     +15 pts    │  │
│  │  ☐ 🥗 Alimentación balanceada                      +15 pts    │  │
│  │  ☑ 💧 Hidratación adecuada            ✓           +15 pts    │  │
│  │  ☑ 😴 Sueño reparador                 ✓           +15 pts    │  │
│  │  ☐ ❤️ Bienestar emocional                          +15 pts    │  │
│  │                                                               │  │
│  │  📊 Progreso: 2/8 completados                                │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 🎯 OBJETIVOS DE SALUD                                         │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                               │  │
│  │  🎯 Reducir presión arterial a 120/80                        │  │
│  │     ████████░░░░░░░░░░░░░░░░░░░░ 30%                        │  │
│  │                                                               │  │
│  │  🎯 HbA1c < 7%                                                │  │
│  │     ██████████████░░░░░░░░░░░░░░ 45%                        │  │
│  │                                                               │  │
│  │  🎯 Perder 5 kg                                               │  │
│  │     ██████░░░░░░░░░░░░░░░░░░░░░░ 20%                        │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 📋 PROGRAMAS DE SALUD                                         │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                               │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │ 🫀 PROGRAMA DE HIPERTENSIÓN                            │  │  │
│  │  │ Control integral de presión arterial                   │  │  │
│  │  │                                                         │  │  │
│  │  │ ⭐ +100 puntos al inscribirte                          │  │  │
│  │  │                                                         │  │  │
│  │  │ [+ Inscribir] ← CLICK AQUÍ                            │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  │                                                               │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │ 🩺 PROGRAMA DE DIABETES                                 │  │  │
│  │  │ Control integral de glucosa                            │  │  │
│  │  │                                                         │  │  │
│  │  │ ⭐ +100 puntos al inscribirte                          │  │  │
│  │  │                                                         │  │  │
│  │  │ [+ Inscribir]                                          │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  │                                                               │  │
│  │  ... (2 programas más recomendados)                          │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
                  [CLICK EN "+ INSCRIBIR" EN HIPERTENSIÓN]
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│                  ⚡ MODAL DE INSCRIPCIÓN ⚡                         │
│                  Ventana Emergente (Overlay)                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ╔══════════════════════════════════════════════════════════════╗  │
│  ║  Programa de Hipertensión                                     ║  │
│  ║  Selecciona tu ciudad, clínica y horario preferido            ║  │
│  ╚══════════════════════════════════════════════════════════════╝  │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 📍 Ciudad                                                     │  │
│  │                                                               │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │ Seleccione una ciudad                               ▼ │  │  │
│  │  ├────────────────────────────────────────────────────────┤  │  │
│  │  │ Bogotá                                                 │  │  │
│  │  │ Medellín                                               │  │  │
│  │  │ Cali                                                   │  │  │
│  │  │ Barranquilla                                           │  │  │
│  │  │ Cartagena                                              │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                   ↓ [Usuario selecciona Bogotá]                     │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 🏥 Clínica Colsanitas                                         │  │
│  │                                                               │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │ Seleccione una clínica                              ▼ │  │  │
│  │  ├────────────────────────────────────────────────────────┤  │  │
│  │  │ Clínica Reina Sofía                                    │  │  │
│  │  │ Clínica Universitaria Colombia                         │  │  │
│  │  │ Clínica La Colina                                      │  │  │
│  │  │ Centro Médico Colsanitas El Polo                       │  │  │
│  │  │ Centro Médico Colsanitas Suba                          │  │  │
│  │  │ Clínica Infantil Colsubsidio                           │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  └──────────────────────────────────────────────────────────────┘  │
│            ↓ [Usuario selecciona Clínica Reina Sofía]              │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 🕐 Horario de Preferencia                                     │  │
│  │                                                               │  │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐                  │  │
│  │  │ 7:00-9:00 │ │ 9:00-11:00│ │11:00-1:00 │                  │  │
│  │  └───────────┘ └───────────┘ └───────────┘                  │  │
│  │                                                               │  │
│  │  ┌───────────┐ ┌───────────┐ ┌───────────┐                  │  │
│  │  │ 2:00-4:00 │ │ 4:00-6:00 │ │ 6:00-8:00 │                  │  │
│  │  └───────────┘ └───────────┘ └───────────┘                  │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│         ↓ [Usuario selecciona 9:00 AM - 11:00 AM]                  │
│                                                                      │
│  ╔══════════════════════════════════════════════════════════════╗  │
│  ║ 📋 Resumen de Inscripción                                     ║  │
│  ╠══════════════════════════════════════════════════════════════╣  │
│  ║ Programa:  Programa de Hipertensión                           ║  │
│  ║ Ciudad:    Bogotá                                             ║  │
│  ║ Clínica:   Clínica Reina Sofía                                ║  │
│  ║ Horario:   9:00 AM - 11:00 AM                                 ║  │
│  ╚══════════════════════════════════════════════════════════════╝  │
│                                                                      │
│  ┌──────────────┐  ┌───────────────────────────────────────────┐  │
│  │  [Cancelar]  │  │  [Confirmar Inscripción] ← ACTIVO        │  │
│  └──────────────┘  └───────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
                  [CLICK EN "CONFIRMAR INSCRIPCIÓN"]
                              ↓
                       ⚡ MODAL SE CIERRA ⚡
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│     PANTALLA 5: TAMAGOTCHI - MARÍA (ACTUALIZADA)                   │
│     Ahora inscrita en Hipertensión                                  │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ╔══════════════════════════════════════════════════════════════╗  │
│  ║              👩 AVATAR GIGANTE (Flotando)                    ║  │
│  ║                                                               ║  │
│  ║  MARÍA GONZÁLEZ - 45 años - Bogotá                           ║  │
│  ║  Estado: 😊 Feliz                                             ║  │
│  ║                                                               ║  │
│  ║  ████████████░░░░░ 65% Salud                                 ║  │
│  ║  ⭐ 950 puntos (+100) | 🏆 Nivel 3 | 🔥 7 días              ║  │
│  ╚══════════════════════════════════════════════════════════════╝  │
│                                                                      │
│  ... (Hábitos y Objetivos - igual que antes)                        │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 📋 PROGRAMAS DE SALUD                                         │  │
│  ├──────────────────────────────────────────────────────────────┤  │
│  │                                                               │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │ 🫀 PROGRAMA DE HIPERTENSIÓN                            │  │  │
│  │  │ Control integral de presión arterial                   │  │  │
│  │  │                                                         │  │  │
│  │  │ ✅ Inscrito en: Clínica Reina Sofía (Bogotá)          │  │  │
│  │  │ 🕐 Horario: 9:00 AM - 11:00 AM                         │  │  │
│  │  │                                                         │  │  │
│  │  │ [✓ Inscrito] (Deshabilitado)                          │  │  │
│  │  │                                                         │  │  │
│  │  │ ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━  │  │  │
│  │  │                                                         │  │  │
│  │  │ ✅ TAREAS DEL PROGRAMA:                                │  │  │
│  │  │                                                         │  │  │
│  │  │ ☐ 📊 Registrar toma de presión arterial   +25 pts     │  │  │
│  │  │ ☐ 💊 Confirmar adherencia a medicamentos  +25 pts     │  │  │
│  │  │ ☐ 📅 Agendar control cardiología          +25 pts     │  │  │
│  │  │                                                         │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  │                                                               │  │
│  │  ... (otros programas)                                        │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
                              ↓
            [CLICK EN "📊 Registrar toma de presión arterial"]
                              ↓

┌─────────────────────────────────────────────────────────────────────┐
│              ⚡ ANIMACIÓN DE GAMIFICACIÓN ⚡                        │
├─────────────────────────────────────────────────────────────────────┤
│                                                                      │
│  ╔══════════════════════════════════════════════════════════════╗  │
│  ║              👩 AVATAR GIGANTE (Saltando feliz)              ║  │
│  ║                                                               ║  │
│  ║  MARÍA GONZÁLEZ - 45 años - Bogotá                           ║  │
│  ║  Estado: 😊 Feliz                                             ║  │
│  ║                                                               ║  │
│  ║  █████████████░░░ 66% Salud (+1%)                            ║  │
│  ║  ⭐ 975 puntos (+25) | 🏆 Nivel 3 | 🔥 7 días               ║  │
│  ╚══════════════════════════════════════════════════════════════╝  │
│                                                                      │
│  ... (Hábitos y Objetivos)                                          │
│                                                                      │
│  ┌──────────────────────────────────────────────────────────────┐  │
│  │ 📋 PROGRAMAS DE SALUD                                         │  │
│  │                                                               │  │
│  │  ┌────────────────────────────────────────────────────────┐  │  │
│  │  │ 🫀 PROGRAMA DE HIPERTENSIÓN                            │  │  │
│  │  │                                                         │  │  │
│  │  │ ✅ TAREAS DEL PROGRAMA:                                │  │  │
│  │  │                                                         │  │  │
│  │  │ ☑ 📊 Registrar toma de presión arterial   ✓ +25 pts   │  │  │
│  │  │   └─ (Fondo verde, checkbox marcado)                   │  │  │
│  │  │                                                         │  │  │
│  │  │ ☐ 💊 Confirmar adherencia a medicamentos  +25 pts     │  │  │
│  │  │ ☐ 📅 Agendar control cardiología          +25 pts     │  │  │
│  │  │                                                         │  │  │
│  │  │ 📊 Progreso: 1/3 tareas completadas                    │  │  │
│  │  └────────────────────────────────────────────────────────┘  │  │
│  │                                                               │  │
│  └──────────────────────────────────────────────────────────────┘  │
│                                                                      │
└─────────────────────────────────────────────────────────────────────┘
```

---

## 📊 TABLA DE TRANSICIONES

| De | Acción | A | Duración |
|----|--------|---|----------|
| **P1** Chat | Click "Ver Gemelo Digital" | **P2** Selección de Rol | Instantáneo |
| **P2** Selección | Click "Individual" | **P4** Dashboard (1 perfil) | Instantáneo |
| **P2** Selección | Click "Gestor Familiar" | **P3** Autorización | Instantáneo |
| **P3** Autorización | Marcar 3 checkboxes + Continuar | **P4** Dashboard (4 perfiles) | Instantáneo |
| **P4** Dashboard | Click en tarjeta de familiar | **P5** Tamagotchi Detallado | Animación 0.3s |
| **P5** Tamagotchi | Click "Volver" | **P4** Dashboard | Instantáneo |
| **P5** Tamagotchi | Click [+ Inscribir] | **Modal** Inscripción | Slide-in 0.3s |
| **Modal** | Click "Cancelar" | **P5** Tamagotchi (sin cambios) | Slide-out 0.3s |
| **Modal** | Click "Confirmar" | **P5** Tamagotchi (actualizado) | Slide-out 0.3s |
| **P5** Tamagotchi | Click checkbox hábito | **P5** (puntos +15, salud +2%) | Animación 0.2s |
| **P5** Tamagotchi | Click checkbox tarea | **P5** (puntos +25, salud +1%) | Animación 0.2s |

---

## 🎮 SISTEMA DE PUNTOS - FLUJO VISUAL

```
INICIO: María tiene 850 puntos, 65% salud, Nivel 3

    ↓

ACCIÓN 1: Marca hábito "💧 Hidratación"
    ├─ +15 puntos → 865 puntos
    ├─ +2% salud → 67% salud
    └─ Nivel 3 (sin cambio)

    ↓

ACCIÓN 2: Se inscribe en "Programa de Hipertensión"
    ├─ +100 puntos → 965 puntos
    ├─ Salud sin cambio → 67% salud
    └─ Nivel 3 (sin cambio, necesita 1,001 para Nivel 4)

    ↓

ACCIÓN 3: Completa tarea "Registrar presión arterial"
    ├─ +25 puntos → 990 puntos
    ├─ +1% salud → 68% salud
    └─ Nivel 3 (a 11 puntos de Nivel 4)

    ↓

RESULTADO FINAL (en 3 minutos):
    ├─ 📈 Puntos: 850 → 990 (+140 pts)
    ├─ 📈 Salud: 65% → 68% (+3%)
    ├─ 📈 Hábitos: 2 → 3 completados
    ├─ 📈 Programas: 0 → 1 inscrito
    └─ 📈 Tareas: 0 → 1 completada
```

---

## 🔄 CICLO DE ENGAGEMENT DIARIO

```
DÍA 1                              DÍA 2                              DÍA 3
─────────────────────────────────────────────────────────────────────────

Usuario entra           →   Usuario entra           →   Usuario entra
    ↓                           ↓                           ↓
Ve racha de 7 días              Racha sigue: 8 días         Racha sigue: 9 días
    ↓                           ↓                           ↓
Marca 3 hábitos                 Marca 4 hábitos             Marca 5 hábitos
+45 pts, +6% salud             +60 pts, +8% salud          +75 pts, +10% salud
    ↓                           ↓                           ↓
Completa 2 tareas               Completa 2 tareas           Completa 3 tareas
+50 pts, +2% salud             +50 pts, +2% salud          +75 pts, +3% salud
    ↓                           ↓                           ↓
TOTAL DÍA: +95 pts             TOTAL DÍA: +110 pts         TOTAL DÍA: +150 pts
           +8% salud                      +10% salud                 +13% salud
    ↓                           ↓                           ↓
Avatar más feliz 😊             Barras de objetivos suben   ¡Sube de nivel! 🏆
    ↓                           ↓                           ↓
Usuario satisfecho              Usuario motivado            Usuario adicto
    ↓                           ↓                           ↓
Vuelve mañana                   Vuelve mañana               Vuelve mañana
```

---

## 📊 DATOS CAPTURADOS EN CADA PASO

### PANTALLA 1: Chat
- Mensajes enviados por usuario
- Objeciones expresadas
- Tiempo en conversación
- Palabras clave de aceptación

### PANTALLA 2: Selección de Rol
- Rol elegido (Individual vs Familiar)
- Timestamp de decisión

### PANTALLA 3: Autorización
- Checkboxes marcados
- Tiempo para aceptar términos
- Timestamp de consentimiento

### PANTALLA 4: Dashboard
- Familiar seleccionado para ver
- Tiempo en dashboard
- Orden de visualización

### PANTALLA 5: Tamagotchi
- Hábitos completados (IDs)
- Tareas completadas (IDs)
- Programas inscritos (códigos)
- **Datos de enrollment por programa:**
  - Ciudad seleccionada
  - Clínica seleccionada
  - Horario seleccionado
  - Timestamp de inscripción
- Puntos acumulados
- Salud alcanzada
- Nivel alcanzado
- Racha de días
- Tiempo total en sesión

---

## 🎯 MÉTRICAS CLAVE DEL FLUJO

### Conversión por Pantalla:

```
100 usuarios inician en P1
    ↓
85 usuarios llegan a P2 (Tasa de conversión: 85%)
    ↓
70 usuarios aceptan en P3 (Tasa de conversión: 82%)
    ↓
70 usuarios ven dashboard P4 (Tasa de conversión: 100%)
    ↓
65 usuarios abren Tamagotchi P5 (Tasa de conversión: 93%)
    ↓
55 usuarios marcan 1 hábito (Tasa de conversión: 85%)
    ↓
50 usuarios se inscriben en 1 programa (Tasa de conversión: 91%)
    ↓
45 usuarios completan 1 tarea (Tasa de conversión: 90%)
```

**CONVERSIÓN TOTAL: 45% (45 de 100 completan toda la experiencia)**

---

## ✨ ANIMACIONES Y FEEDBACK VISUAL

### Al marcar checkbox:
```
Estado inicial → Click → Animación (0.2s) → Estado final
[ ] Gris       →  👆  → ✓ Verde parpadeando → [✓] Verde sólido
```

### Al inscribirse en programa:
```
Botón inicial → Click → Modal → Confirmar → Botón final
[+ Inscribir] →  👆  → Overlay → +100 pts → [✓ Inscrito]
  (Verde)                        (Animación)   (Gris)
```

### Al subir de nivel:
```
Nivel 3 → +25 pts → Alcanza 1,001 pts → Animación → Nivel 4
  🏆                                      ⭐✨🎉      🏆🏆
```

### Avatar según salud:
```
0-59%:  😟 Triste    (Rojo)
60-79%: 😐 Neutral   (Amarillo)
80-100%: 😊 Feliz    (Verde)
```

---

**FIN DEL FLUJO VISUAL**

---

*Plataforma Integrada - Gemelo Digital + Tamagotchi Familiar*
*Versión 1.0 - 19 de Noviembre 2025*
*1,782 líneas de código - 100% funcional*
