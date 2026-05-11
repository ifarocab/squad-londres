---
name: issue-status-standard
description: Standard skill for issue status transitions, executable detection, and flow gates using squad scripts from 02.issue_status_update. Use when deciding next executable issue, moving statuses, or auditing in-progress integrity.
---

# Issue Status Standard

## Fuente de scripts (baseline)
Usar scripts de:
`C:\Users\ifaro\OneDrive\Documentos\02.GitHub_Repository\00. Ai_engineering\03.Scripts\00.agent_tools\02.issue_status_update`

## Casos de uso
- Detectar siguiente hoja ejecutable (`get_next_executable.py`).
- Auditar WIP real (`audit_inprogress.py`).
- Aplicar gates de estado (`issue_gatekeeper.py`, `orchestrate_checklist.py`).
- Ajustar estados con script (`update_issue_status.ps1`).

## Flujo
1. Detectar issue ejecutable o bloqueo real.
2. Validar gate de estado antes de mover la issue.
3. Aplicar transición de estado.
4. Verificar evidencia y dependencia.
5. Registrar trazabilidad mínima.

## Reglas
- Prohibido `in progress` sin evidencia nueva.
- Owner único obligatorio.
- Si bloqueo > SLA, escalar o reasignar.

## Referencias
- `references/script-inventory.md`
- `references/status-gates.md`
