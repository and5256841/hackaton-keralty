# 🔐 CREDENCIALES DE ACCESO
## Gemelo Digital - Plataforma de Salud

---

## 🚀 INICIO RÁPIDO

```bash
# Ejecutar:
ABRIR_PLATAFORMA.bat

# Aparecerá pantalla de login
# Usar cualquiera de estas 3 credenciales:
```

---

## 👥 CREDENCIALES VÁLIDAS

### 1. Usuario Principal (Recomendado para Demo)
```
Usuario:    admin
Contraseña: hackathon2025
```
**Uso:** Presentaciones a jueces, demos oficiales, primera impresión

---

### 2. Usuario de Prueba Rápida
```
Usuario:    demo
Contraseña: 2025
```
**Uso:** Testing interno, pruebas rápidas, desarrollo

---

### 3. Usuario para Cliente/Stakeholder
```
Usuario:    colsanitas
Contraseña: gemelo2025
```
**Uso:** Demos a clientes, stakeholders, inversores

---

## 📋 INSTRUCCIONES DE USO

### Paso 1: Abrir la Plataforma
- Doble clic en `ABRIR_PLATAFORMA.bat`
- O abrir directamente: `frontend/index.html`

### Paso 2: Pantalla de Login
Verás:
```
🔐 Acceso al Sistema
Gemelo Digital - Plataforma Segura

┌─────────────────────────┐
│ Usuario:                 │
│ [___________________]   │
│                         │
│ Contraseña:             │
│ [___________________]   │
│                         │
│  [Ingresar al Sistema]  │
└─────────────────────────┘

💡 Credenciales de Demo
Usuario: admin | Contraseña: hackathon2025
```

### Paso 3: Ingresar
1. Escribir usuario en el primer campo
2. Escribir contraseña en el segundo campo
3. Click en "Ingresar al Sistema 🚀" o presionar Enter

### Paso 4: Acceso Concedido
- Transición suave (300ms)
- Landing page se muestra
- Sesión se mantiene al recargar (F5)

---

## ✅ LOGIN EXITOSO

**Señales de éxito:**
- ✅ Pantalla de login desaparece suavemente
- ✅ Landing page aparece con animación fade-in
- ✅ Puedes ver las 2 tarjetas (Paciente / Administrador)
- ✅ Partículas animadas en el fondo

---

## ❌ LOGIN FALLIDO

**Qué pasa si las credenciales son incorrectas:**
- ❌ Mensaje de error: "Usuario o contraseña incorrectos"
- Animación de sacudida (shake) del mensaje
- Campo de contraseña se limpia automáticamente
- Puedes intentar de nuevo
- Mensaje desaparece después de 3 segundos

**Soluciones:**
1. Verifica que no haya espacios extra
2. Las credenciales son case-sensitive (admin ≠ Admin)
3. Copia y pega las credenciales de arriba
4. Prueba con otra credencial (demo/2025)

---

## 🔄 CERRAR SESIÓN

**Opción 1: Cerrar pestaña del navegador**
- Cierra la pestaña o ventana
- Al volver a abrir, verás el login nuevamente

**Opción 2: Limpiar SessionStorage (Avanzado)**
1. Presiona F12 (DevTools)
2. Ve a la pestaña "Console"
3. Escribe:
   ```javascript
   sessionStorage.clear();
   location.reload();
   ```
4. Presiona Enter

---

## 💡 TIPS PARA HACKATHON

### Para Jueces (Demo Oficial)
✅ **Usar:** admin / hackathon2025
- Muestra profesionalismo
- Nombre de credencial memorable
- Relacionado con el evento

### Para Testing Rápido
✅ **Usar:** demo / 2025
- Más rápido de escribir
- Ideal para pruebas internas
- Menos caracteres

### Para Clientes/Inversores
✅ **Usar:** colsanitas / gemelo2025
- Personalizado para el cliente
- Demuestra que pensaste en ellos
- Credenciales "branded"

---

## 🎯 SCRIPT DE DEMO (15 segundos)

**Qué decir mientras haces login:**

> "Nuestra plataforma cuenta con autenticación segura. Como pueden ver, las credenciales de demostración están visibles en pantalla. Voy a ingresar con el usuario 'admin' y contraseña 'hackathon2025'."
>
> [Escribir credenciales]
>
> [Click en "Ingresar al Sistema"]
>
> "Y ahora tenemos acceso completo a la plataforma."
>
> [Continuar con demo de la landing page]

---

## 🛠️ TROUBLESHOOTING

### Problema: "No me deja entrar"
**Causas posibles:**
- Espacios extra al copiar/pegar
- Mayúsculas incorrectas
- Contraseña incorrecta

**Solución:**
```
Intenta con estas credenciales exactas:
admin
hackathon2025

O usa la alternativa:
demo
2025
```

---

### Problema: "Me saca cada vez que recargo"
**Causa:** Navegador en modo incógnito

**Solución:** Usa ventana normal (no privada/incógnito)

---

### Problema: "Quiero agregar más usuarios"
**Solución:**

1. Abrir `frontend/index.html` en un editor
2. Buscar línea ~380:
   ```javascript
   const VALID_CREDENTIALS = {
       'admin': 'hackathon2025',
       'demo': '2025',
       'colsanitas': 'gemelo2025'
   };
   ```
3. Agregar nueva línea:
   ```javascript
   const VALID_CREDENTIALS = {
       'admin': 'hackathon2025',
       'demo': '2025',
       'colsanitas': 'gemelo2025',
       'miUsuario': 'miPassword'  // ← Nuevo usuario
   };
   ```
4. Guardar archivo
5. Recargar página (F5)

---

## 📊 CARACTERÍSTICAS DE SEGURIDAD

### ✅ Implementado (MVP)
- Validación client-side de credenciales
- Campo de contraseña oculto (type="password")
- Limpieza automática en error
- SessionStorage para persistencia
- No almacena contraseñas en localStorage

### ⚠️ Limitaciones (Demo/Hackathon)
- Credenciales visibles en código fuente
- No hay backend real
- No hay rate limiting
- No hay recuperación de contraseña
- SessionStorage (temporal)

**Nota:** Esto es un MVP para demostración. En producción se requeriría backend con autenticación real, JWT tokens, bcrypt para passwords, HTTPS, etc.

---

## 📞 CONTACTO DE EMERGENCIA

**Si tienes problemas durante el hackathon:**

1. Verifica que estás usando navegador moderno (Chrome, Firefox, Edge)
2. Intenta con modo incógnito deshabilitado
3. Prueba las 3 credenciales una por una
4. Refresca la página (F5)
5. Cierra y vuelve a abrir el navegador

**Si nada funciona:**
- Usa acceso directo sin login: `ABRIR_PLATAFORMA_INTEGRADA.bat` (paciente) o `ABRIR_DASHBOARD_ADMIN.bat` (admin)

---

## 🎉 RESUMEN EJECUTIVO

### 3 Credenciales Válidas:
1. **admin** / hackathon2025 (Principal)
2. **demo** / 2025 (Rápida)
3. **colsanitas** / gemelo2025 (Cliente)

### Tiempo de login: 5-10 segundos
### Complejidad: Muy baja
### Profesionalismo: Alto
### Seguridad: Básica (suficiente para MVP)

---

**IMPORTANTE:** Imprime este archivo o tenlo a mano durante el hackathon para referencia rápida.

---

**VERSIÓN:** 1.0 - Sistema de Autenticación
**FECHA:** 19 de Noviembre 2025
**ESTADO:** ✅ Funcional y documentado

---

*Gemelo Digital - Plataforma Segura*
*Credenciales listas para usar - Demo de Hackathon 2025*
