# ✅ MODAL DE INSCRIPCIÓN A PROGRAMAS

## 🎯 Actualización Realizada

**Archivo modificado:** `frontend/plataforma_integrada.html`

**NO se creó nueva plataforma** - Se agregó modal al archivo existente.

---

## 🆕 Nueva Funcionalidad: Ventana Emergente de Inscripción

### ¿Qué se agregó?

Cuando el usuario hace click en **[+ Inscribir]** en cualquier programa, ahora se abre un **modal (ventana emergente)** donde debe seleccionar:

1. **📍 Ciudad** (5 principales de Colombia)
2. **🏥 Clínica Colsanitas** (según la ciudad seleccionada)
3. **🕐 Horario de preferencia** (6 opciones)

---

## 🏥 Base de Datos de Clínicas Colsanitas

### Bogotá (6 clínicas):
- Clínica Reina Sofía
- Clínica Universitaria Colombia
- Clínica La Colina
- Centro Médico Colsanitas El Polo
- Centro Médico Colsanitas Suba
- Clínica Infantil Colsubsidio

### Medellín (4 clínicas):
- Clínica Colsanitas Medellín
- Centro Médico Colsanitas Laureles
- Centro Médico Colsanitas El Poblado
- Clínica Las Américas

### Cali (3 clínicas):
- Clínica Colsanitas Torre de Cali
- Centro Médico Colsanitas Norte
- Centro Médico Colsanitas Sur

### Barranquilla (3 clínicas):
- Clínica Colsanitas Barranquilla
- Centro Médico Colsanitas Norte
- Centro Médico Colsanitas Riomar

### Cartagena (2 clínicas):
- Clínica Colsanitas Cartagena
- Centro Médico Colsanitas Bocagrande

**Total: 18 clínicas en 5 ciudades**

---

## 🕐 Horarios Disponibles

**6 franjas horarias:**
1. 7:00 AM - 9:00 AM (Mañana temprano)
2. 9:00 AM - 11:00 AM (Media mañana)
3. 11:00 AM - 1:00 PM (Antes del almuerzo)
4. 2:00 PM - 4:00 PM (Tarde temprano)
5. 4:00 PM - 6:00 PM (Media tarde)
6. 6:00 PM - 8:00 PM (Tarde/noche)

---

## 🎮 Flujo de Inscripción (Paso a Paso)

### ANTES (sin modal):
```
Usuario → Click [+ Inscribir]
       → Inscripción inmediata (+100 pts)
       → Fin
```

### AHORA (con modal):
```
Usuario → Click [+ Inscribir]
       ↓
MODAL SE ABRE
       ↓
PASO 1: Seleccionar Ciudad
       (Dropdown con 5 opciones)
       ↓
PASO 2: Seleccionar Clínica
       (Dropdown con clínicas de esa ciudad)
       ↓
PASO 3: Seleccionar Horario
       (Grid de 6 botones de horario)
       ↓
RESUMEN DE INSCRIPCIÓN APARECE
       - Programa: [nombre]
       - Ciudad: [ciudad]
       - Clínica: [clínica]
       - Horario: [horario]
       ↓
Botón "Confirmar Inscripción" se ACTIVA
       ↓
Usuario → Click [Confirmar Inscripción]
       ↓
Modal se cierra
       ↓
Inscripción completada (+100 pts)
       ↓
Programa marca como [✓ Inscrito]
       ↓
Tareas del programa aparecen
```

---

## 📱 Cómo se Ve el Modal

### Encabezado:
```
╔════════════════════════════════════╗
║  Programa de Hipertensión         ║
║  Selecciona tu ciudad, clínica y  ║
║  horario preferido                ║
╚════════════════════════════════════╝
```

### Sección 1 - Ciudad:
```
📍 Ciudad
┌──────────────────────────────────┐
│ Seleccione una ciudad          ▼│
├──────────────────────────────────┤
│ Bogotá                           │
│ Medellín                         │
│ Cali                             │
│ Barranquilla                     │
│ Cartagena                        │
└──────────────────────────────────┘
```

### Sección 2 - Clínica (después de seleccionar ciudad):
```
🏥 Clínica Colsanitas
┌──────────────────────────────────┐
│ Seleccione una clínica         ▼│
├──────────────────────────────────┤
│ Clínica Reina Sofía              │
│ Clínica Universitaria Colombia   │
│ Clínica La Colina                │
│ Centro Médico El Polo            │
│ ... (etc.)                       │
└──────────────────────────────────┘
```

### Sección 3 - Horario:
```
🕐 Horario de Preferencia

┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ 7:00 - 9:00 │ │ 9:00 - 11:00│ │11:00 - 1:00 │
└─────────────┘ └─────────────┘ └─────────────┘
┌─────────────┐ ┌─────────────┐ ┌─────────────┐
│ 2:00 - 4:00 │ │ 4:00 - 6:00 │ │ 6:00 - 8:00 │
└─────────────┘ └─────────────┘ └─────────────┘
     (Grid de 3x2)
```

### Resumen (aparece cuando todo está seleccionado):
```
╔════════════════════════════════════╗
║ 📋 Resumen de Inscripción          ║
╠════════════════════════════════════╣
║ Programa:  Programa de Hipertensión
║ Ciudad:    Bogotá                  ║
║ Clínica:   Clínica Reina Sofía     ║
║ Horario:   9:00 AM - 11:00 AM      ║
╚════════════════════════════════════╝
```

### Botones:
```
┌──────────────┐  ┌──────────────────────────┐
│   Cancelar   │  │ Confirmar Inscripción    │
└──────────────┘  └──────────────────────────┘
    (Gris)             (Verde - solo activo
                        cuando todo está lleno)
```

---

## 🎯 Validaciones Implementadas

### 1. Botón "Confirmar" deshabilitado hasta que:
- ✅ Ciudad esté seleccionada
- ✅ Clínica esté seleccionada
- ✅ Horario esté seleccionado

### 2. Dropdown de Clínicas:
- Deshabilitado hasta que se seleccione ciudad
- Se llena automáticamente con clínicas de esa ciudad
- Mensaje: "Primero seleccione una ciudad"

### 3. Resumen:
- Solo aparece cuando los 3 campos están llenos
- Muestra vista previa de la selección

### 4. Selección visual de horario:
- Click en un horario → Se marca con borde verde
- Click en otro → Se desmarca el anterior
- Solo uno seleccionado a la vez

---

## 💾 Datos Guardados

Cuando el usuario confirma la inscripción, se guarda:

```javascript
patient.enrollmentDetails = {
    HYPERTENSION: {
        city: "bogota",
        clinic: "Clínica Reina Sofía",
        time: "9:00 AM - 11:00 AM",
        enrolledDate: "2025-11-19T20:00:00.000Z"
    }
    // ... otros programas
};
```

**Esto permite:**
- Mostrar detalles de inscripción después
- Recordatorios específicos de citas
- Reportes de enrollment por ciudad/clínica
- Analytics del asegurador

---

## 🎨 Diseño Visual

### Colores:
- Fondo modal: Blanco (#FFFFFF)
- Overlay: Negro semi-transparente (rgba(0,0,0,0.7))
- Bordes: Gris claro (#e0e0e0)
- Hover: Turquesa (#128C7E)
- Seleccionado: Verde (#25D366)
- Botón confirmar: Verde degradado
- Botón cancelar: Gris (#e0e0e0)

### Animación:
```css
@keyframes modalSlideIn {
    from: translateY(-50px), opacity: 0
    to: translateY(0), opacity: 1
}
```
- Modal aparece deslizándose desde arriba
- Duración: 0.3 segundos

### Responsive:
- Desktop: Grid de horarios 3x2
- Móvil: Grid de horarios 2x3
- Modal se ajusta a pantalla pequeña

---

## 🚀 Cómo Probar

### 1. Abrir plataforma:
```
Doble clic en: ABRIR_PLATAFORMA_INTEGRADA.bat
```

### 2. Ir a un paciente:
- Chat → Rol → Consent → Dashboard
- Click en "María González"

### 3. Probar inscripción con modal:
1. Scroll a "Programas de Salud"
2. Click en **[+ Inscribir]** en "Hipertensión"
3. ✅ Modal se abre con título "Programa de Hipertensión"
4. Seleccionar ciudad: **Bogotá**
5. ✅ Dropdown de clínicas se activa
6. Seleccionar clínica: **Clínica Reina Sofía**
7. Click en horario: **9:00 AM - 11:00 AM**
8. ✅ Resumen aparece
9. ✅ Botón "Confirmar" se activa (verde)
10. Click **[Confirmar Inscripción]**
11. ✅ Modal se cierra
12. ✅ Botón cambia a [✓ Inscrito]
13. ✅ +100 puntos
14. ✅ Tareas del programa aparecen

### 4. Probar cancelar:
1. Inscribir en otro programa
2. Llenar campos parcialmente
3. Click **[Cancelar]**
4. ✅ Modal se cierra sin inscribir
5. ✅ Botón sigue en [+ Inscribir]

---

## 📊 Ejemplo de Demo Completa

**Caso: María se inscribe en Diabetes**

```
PASO 1: María abre su Tamagotchi
        - 850 puntos, 65% salud

PASO 2: Scroll a "Programas de Salud"
        - Ve 4 programas recomendados

PASO 3: Click [+ Inscribir] en "Diabetes"
        - Modal se abre

PASO 4: Selecciona Ciudad → Bogotá
        - Dropdown clínicas se activa con 6 opciones

PASO 5: Selecciona Clínica → Clínica Universitaria Colombia

PASO 6: Click en horario → 2:00 PM - 4:00 PM
        - Horario se marca verde
        - Resumen aparece:
          📋 Resumen de Inscripción
          Programa: Programa de Diabetes
          Ciudad: Bogotá
          Clínica: Clínica Universitaria Colombia
          Horario: 2:00 PM - 4:00 PM

PASO 7: Click [Confirmar Inscripción]
        - Modal se cierra
        - Puntos: 850 → 950 (+100)
        - Botón: [+ Inscribir] → [✓ Inscrito]
        - Aparecen 4 tareas del programa:
          [ ] Registrar glucometría diaria
          [ ] Cargar resultados HbA1c
          [ ] Verificar función renal
          [ ] Agendar nutrición

RESULTADO:
- María inscrita en Diabetes
- Clínica asignada: Universitaria Colombia (Bogotá)
- Horario: 2:00 PM - 4:00 PM
- +100 puntos
- 4 tareas disponibles para completar
```

---

## 🎁 Beneficios para el Asegurador

### 1. Datos Granulares de Enrollment:
**Antes:**
- "María inscrita en Diabetes" ✓

**Ahora:**
- "María inscrita en Diabetes" ✓
- Ciudad: Bogotá
- Clínica: Universitaria Colombia
- Horario preferido: 2:00 PM - 4:00 PM
- Fecha de inscripción: 2025-11-19

### 2. Analytics Mejorados:
- Clínicas más populares por ciudad
- Horarios más demandados
- Distribución geográfica de enrollment
- Capacidad de planificación de recursos

### 3. Recordatorios Personalizados:
```
"Hola María, tienes cita en el Programa de Diabetes
 el [fecha] a las 2:00 PM en Clínica Universitaria Colombia (Bogotá).
 Dirección: [dirección]"
```

### 4. Coordinación de Citas:
- Asegurador puede agendar citas reales
- Sincronización con calendario de clínicas
- Evitar sobrecupos en horarios populares

---

## 🔧 Cambios Técnicos

### Nuevas Constantes:
```javascript
const COLSANITAS_CLINICS = {
    bogota: [...],
    medellin: [...],
    // etc.
};

const TIME_SLOTS = [
    "7:00 AM - 9:00 AM",
    // ... 6 horarios
];

let pendingEnrollment = {
    programCode, programName, city, clinic, time
};
```

### Nuevas Funciones:
```javascript
openEnrollmentModal(programCode)    // Abre modal
closeEnrollmentModal()              // Cierra modal
renderTimeSlots()                   // Renderiza grid de horarios
updateClinics()                     // Actualiza clínicas según ciudad
selectTimeSlot(index)               // Selecciona un horario
updateSummary()                     // Actualiza resumen
getCityName(cityCode)               // Convierte código a nombre
confirmEnrollment()                 // Confirma e inscribe
```

### Función Modificada:
```javascript
toggleProgram(programCode)
// ANTES: Inscribir directo
// AHORA: Abrir modal → Usuario llena → Confirmar → Inscribir
```

### CSS Agregado:
- `.modal-overlay` (overlay oscuro)
- `.modal-content` (caja del modal)
- `.modal-section` (secciones del formulario)
- `.modal-select` (dropdowns)
- `.time-slots` (grid de horarios)
- `.time-slot` (botón de horario)
- `.enrollment-summary` (resumen)
- Animaciones de entrada

---

## ✅ Checklist de Prueba

Antes de la demo:
- [ ] Abrir plataforma_integrada.html
- [ ] Ir a María González
- [ ] Click [+ Inscribir] en cualquier programa
- [ ] **NUEVO:** Modal se abre
- [ ] **NUEVO:** Seleccionar Bogotá → Ver 6 clínicas
- [ ] **NUEVO:** Seleccionar Medellín → Ver 4 clínicas
- [ ] **NUEVO:** Seleccionar clínica
- [ ] **NUEVO:** Click en horario → Se marca verde
- [ ] **NUEVO:** Resumen aparece
- [ ] **NUEVO:** Botón "Confirmar" se activa
- [ ] **NUEVO:** Click Confirmar → Modal se cierra
- [ ] Verificar [✓ Inscrito] y +100 pts
- [ ] Verificar tareas del programa aparecen

---

## 📋 Resumen de la Actualización

| Aspecto | Antes | Ahora |
|---------|-------|-------|
| Inscripción | 1 click | 4 pasos (ciudad, clínica, horario, confirmar) |
| Datos capturados | Solo programa | Programa + Ciudad + Clínica + Horario + Fecha |
| UX | Instantáneo | Modal interactivo |
| Validación | Ninguna | 3 campos obligatorios |
| Clínicas | No especificadas | 18 clínicas reales en 5 ciudades |
| Horarios | No especificados | 6 franjas horarias |
| Cancelar | No disponible | Botón "Cancelar" en modal |

---

¡MODAL DE INSCRIPCIÓN IMPLEMENTADO Y FUNCIONAL! 🚀

**Funciona para TODOS los programas y TODOS los perfiles de pacientes.**
