# ORQUESTADOR MULTI-SQUAD

## Documentacion Completa

**Ubicacion**: Squad_Governance/01.workspace-squad/09.Orchestrator_Squads/
**Responsable**: Squad Governance
**Fecha**: 2026-05-05
**Version**: 1.0

---

## 1. RESUMEN EJECUTIVO

Sistema centralizado de orquestacion de issues GitHub para todos los squads.

### Problema Anterior
- Cron jobs con LLM: 85-95% timeouts
- Tiempos: 180+ segundos
- Carga excesiva en gateway

### Solucion
- Scripts Python nativos
- Tiempo: ~5 segundos
- Tasa exito: >95%
- Configurable via .ini

---

## 2. ARQUITECTURA

Task Scheduler -> run-orchestrator.bat -> orchestrator.py -> squads.ini -> Scripts Python -> GitHub API

---

## 3. ESTRUCTURA

09.Orchestrator_Squads/
+-- README.md
+-- config/squads.ini
+-- scripts/
¦   +-- orchestrator.py
¦   +-- todo-executor.py
¦   +-- detect-light.py
¦   +-- detect-deep.py
¦   +-- lib/
+-- wrappers/
+-- logs/

---

## 4. CONFIGURACION

### Variables de Entorno
- GH_TOKEN: Token GitHub

### squads.ini
Configuracion de squads y repositorios.

---

## 5. INSTALACION

1. Verificar GH_TOKEN
2. Configurar squads.ini
3. Ejecutar como Admin: wrappers/setup-task-scheduler.bat

---

## 6. USO

### Ver estado
schtasks /query /tn OpenClaw\OrquestadorMultiSquad /v

### Ejecutar manualmente
schtasks /run /tn OpenClaw\OrquestadorMultiSquad

### Ver logs
type logs\cron\orchestrator-YYYYMMDD.log

---

## 7. GESTION DE SQUADS

Para anadir un squad:
1. Editar config/squads.ini
2. Anadir seccion [SQUAD_NUEVO]
3. Definir repositorios
4. Listo - no requiere reinicio

---

## 8. MANTENIMIENTO

### Eliminar tarea
schtasks /delete /tn OpenClaw\OrquestadorMultiSquad /f

### Recrear tarea
cd wrappers && setup-task-scheduler.bat

---

Documentacion completa del sistema de orquestacion.
