---
name: issue-orchestrator-standard
description: Standard skill to run recurring issue orchestration loops with squad scheduler/orchestrator scripts from 03.sch_orchestrator. Use for automated cycles, scheduler checks, and fallback operational control without relying on gh plugin flows.
---

# Issue Orchestrator Standard

## Fuente de scripts (baseline)
Usar scripts de:
`C:\Users\ifaro\OneDrive\Documentos\02.GitHub_Repository\00. Ai_engineering\03.Scripts\00.agent_tools\03.sch_orchestrator`

y soporte en:
`C:\Users\ifaro\OneDrive\Documentos\02.GitHub_Repository\00. Ai_engineering\03.Scripts\00.agent_tools\orchestrator`

## Flujo
1. Verificar scheduler/orquestador activo.
2. Ejecutar ciclo de detección + acción.
3. Registrar resultado por ciclo (acción real o incidente).
4. Aplicar fallback si falla acceso/tooling.
5. Mantener trazabilidad y escalado por SLA.

## Reglas
- Nunca cerrar ciclo vacío: si falla tooling, registrar incidente + siguiente acción.
- Priorizar scripts del squad sobre flujos plugin.
- Mantener control de SLA T+10/T+20 para bloqueos.

## Referencias
- `references/script-inventory.md`
- `references/operation-modes.md`
