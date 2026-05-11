# GUIA DE OPERACION - ORQUESTADOR MULTI-SQUAD

## INSTALACION RAPIDA

### Paso 1: Verificar Pre-requisitos
`cmd
echo %GH_TOKEN%
python --version
`

### Paso 2: Configurar Squads
Editar: config/squads.ini

### Paso 3: Instalar Tarea (como Admin)
`cmd
cd wrappers
setup-task-scheduler.bat
`

### Paso 4: Verificar
`cmd
schtasks /query /tn OpenClaw\OrquestadorMultiSquad /v
`

## OPERACION DIARIA

### Ver Estado
`cmd
schtasks /query /tn OpenClaw\OrquestadorMultiSquad /v
`

### Ejecutar Manualmente
`cmd
schtasks /run /tn OpenClaw\OrquestadorMultiSquad
`

### Ver Logs
`cmd
type logs\cron\orchestrator-YYYYMMDD.log
`

## ANADIR NUEVO SQUAD

1. Editar config/squads.ini
2. Anadir seccion [SQUAD_NUEVO]
3. Configurar repositorios
4. Listo - automatico

## SOLUCION DE PROBLEMAS

### Error: GH_TOKEN no definido
Solucion: Configurar variable de entorno

### Error: No se encuentra repositorio
Solucion: Verificar nombre en squads.ini

### Tarea no ejecuta
Solucion: Verificar permisos de ejecucion

## COMANDOS UTILES

Eliminar tarea:
schtasks /delete /tn OpenClaw\OrquestadorMultiSquad /f

Ver todas las tareas:
schtasks /query /fo LIST /v

Ejecutar wrapper manual:
wrappers\run-orchestrator.bat
