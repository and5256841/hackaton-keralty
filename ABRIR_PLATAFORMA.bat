@echo off
color 0B
cls

echo ===============================================================
echo.
echo          GEMELO DIGITAL - PLATAFORMA DE SALUD
echo.
echo ===============================================================
echo.
echo  Bienvenido a la plataforma completa de Gemelo Digital
echo.
echo  Selecciona tu modulo:
echo.
echo  1. Plataforma del Paciente (Gamificacion + IA)
echo  2. Dashboard del Administrador (Metricas + KPIs)
echo.
echo  Abriendo landing page de seleccion...
echo.
echo ===============================================================
echo.
timeout /t 2 > nul

cd /d "%~dp0"
start "" "frontend\index.html"

echo.
echo  Landing page abierta en tu navegador
echo.
echo  Selecciona el modulo que deseas usar
echo.
echo  Presiona cualquier tecla para cerrar esta ventana...
pause > nul
