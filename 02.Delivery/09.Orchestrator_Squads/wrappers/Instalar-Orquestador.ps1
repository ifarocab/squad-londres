# Instalador de Orquestador Multi-Squad
# Ejecutar como Administrador

$wrapperPath = "C:\Users\ifaro\.openclaw\workspaces\Squad_Governance\01.workspace-squad\09.Orchestrator_Squads\wrappers"
$action = New-ScheduledTaskAction -Execute "$wrapperPath\run-orchestrator.bat"
$trigger = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 10) -RepetitionDuration (New-TimeSpan -Days 3650)
$principal = New-ScheduledTaskPrincipal -UserId $env:USERNAME -RunLevel Highest
$settings = New-ScheduledTaskSettingsSet -AllowStartIfOnBatteries -DontStopIfGoingOnBatteries -StartWhenAvailable

Register-ScheduledTask -TaskName "OpenClaw\OrquestadorMultiSquad" -Action $action -Trigger $trigger -Principal $principal -Settings $settings -Force

Write-Host "Instalacion completada"
