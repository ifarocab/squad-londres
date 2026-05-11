@echo off
echo ============================================
echo INSTALACION ORQUESTADOR MULTI-SQUAD
echo ============================================
echo.
echo Este script debe ejecutarse como ADMINISTRADOR
echo.
echo Para ejecutar como administrador:
echo 1. Click derecho en este archivo
echo 2. Seleccionar "Ejecutar como administrador"
echo.
echo ============================================
echo.

set ORCH_PATH=C:\Users\ifaro\.openclaw\workspaces\Squad_Governance\01.workspace-squad\09.Orchestrator_Squads
set WRAPPER_PATH=%ORCH_PATH%\wrappers

echo Verificando privilegios de administrador...
net session >nul 2>&1
if %ERRORLEVEL% neq 0 (
    echo.
    echo ERROR: Este script requiere privilegios de administrador
    echo Por favor, ejecute como administrador
    echo.
    pause
    exit /b 1
)

echo OK: Privilegios de administrador confirmados
echo.
echo ============================================
echo Creando tarea programada...
echo ============================================
echo.

schtasks /create /tn "OpenClaw\OrquestadorMultiSquad" /tr "%WRAPPER_PATH%\run-orchestrator.bat" /sc minute /mo 10 /ru "%USERNAME%" /f /rl HIGHEST

if %ERRORLEVEL% equ 0 (
    echo.
    echo ============================================
    echo INSTALACION EXITOSA
echo ============================================
    echo.
    echo Tarea creada: OpenClaw\OrquestadorMultiSquad
    echo Frecuencia: Cada 10 minutos
    echo Ubicacion: %WRAPPER_PATH%\run-orchestrator.bat
    echo.
    echo El orquestador gestionara los squads configurados en:
    echo %ORCH_PATH%\config\squads.ini
    echo.
    echo Proxima ejecucion: En los proximos 10 minutos
    echo.
) else (
    echo.
    echo ============================================
    echo ERROR EN INSTALACION
echo ============================================
    echo.
    echo Codigo de error: %ERRORLEVEL%
    echo.
)

echo Comandos utiles:
echo   Ver estado:   schtasks /query /tn "OpenClaw\OrquestadorMultiSquad" /v
    echo   Ejecutar:     schtasks /run /tn "OpenClaw\OrquestadorMultiSquad"
echo   Eliminar:     schtasks /delete /tn "OpenClaw\OrquestadorMultiSquad" /f
echo.
pause
