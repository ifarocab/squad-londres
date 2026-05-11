@echo off
setlocal

set ORCH_PATH=C:\Users\ifaro\.openclaw\workspaces\Squad_Governance\01.workspace-squad\09.Orchestrator_Squads
set LOGDIR=%ORCH_PATH%\logs

cd /d "%ORCH_PATH%"

if not exist "%LOGDIR%" mkdir "%LOGDIR%"

echo [%date% %time%] Iniciando Orquestador Multi-Squad >> "%LOGDIR%\orchestrator.log"

python "%ORCH_PATH%\scripts\orchestrator.py" >> "%LOGDIR%\orchestrator.log" 2>&1

set EXITCODE=%ERRORLEVEL%
echo [%date% %time%] Finalizado con codigo: %EXITCODE% >> "%LOGDIR%\orchestrator.log"
echo --- >> "%LOGDIR%\orchestrator.log"

exit /b %EXITCODE%
