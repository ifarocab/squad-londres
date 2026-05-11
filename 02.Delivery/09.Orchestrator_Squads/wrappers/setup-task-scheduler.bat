@echo off
echo ==========================================
echo Configuracion de Task Scheduler
echo Orquestador Multi-Squad - Squad Governance
echo ==========================================
echo.

set ORCH_PATH=C:\Users\ifaro\.openclaw\workspaces\Squad_Governance\01.workspace-squad\09.Orchestrator_Squads
set WRAPPER_PATH=%ORCH_PATH%\wrappers

echo Creando tarea programada...
echo.

schtasks /create /tn "OpenClaw\OrquestadorMultiSquad" /tr "%WRAPPER_PATH%\run-orchestrator.bat" /sc minute /mo 10 /ru "%USERNAME%" /f /rl HIGHEST 2>nul

if %ERRORLEVEL% equ 0 (
    echo OK: Tarea creada exitosamente
    echo.
    echo Nombre: OpenClaw\OrquestadorMultiSquad
    echo Frecuencia: Cada 10 minutos
    echo Ubicacion: %WRAPPER_PATH%\run-orchestrator.bat
    echo.
    echo El orquestador:
    echo   - Lee config desde Squad Governance
    echo   - Gestiona issues de multiples squads
    echo   - Usa GH_TOKEN para GitHub API
) else (
    echo ERROR: No se pudo crear la tarea
    echo Ejecutar como Administrador
)

echo.
echo Comandos utiles:
echo   schtasks /query /tn "OpenClaw\OrquestadorMultiSquad" /v
echo   schtasks /run /tn "OpenClaw\OrquestadorMultiSquad"
echo   schtasks /delete /tn "OpenClaw\OrquestadorMultiSquad" /f
echo.
pause
