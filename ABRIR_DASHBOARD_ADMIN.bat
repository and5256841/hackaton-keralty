@echo off
color 0B
cls

echo ===============================================================
echo.
echo     DASHBOARD ADMINISTRADOR - GEMELO DIGITAL
echo.
echo ===============================================================
echo.
echo  Modulo de Administrador con Metricas y KPIs
echo.
echo  - 30 pacientes sinteticos
echo  - 6 KPIs principales
echo  - 4 graficos de visualizacion
echo  - Filtros y busqueda en tiempo real
echo  - Exportacion a CSV
echo.
echo ===============================================================
echo.
echo  Abriendo dashboard de administrador...
echo.
timeout /t 2 > nul

cd /d "%~dp0"
start "" "frontend\admin_dashboard.html"

echo.
echo  Dashboard abierto en tu navegador
echo.
echo  Presiona cualquier tecla para cerrar esta ventana...
pause > nul
