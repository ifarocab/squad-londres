---
name: issue-update-standard
description: Standard skill to modify existing GitHub issues in ifarocab/Exis using the squad script baseline (01.issue_update). Use when updating issue body, comments, metadata text, or standardized templates. Prefer this over ad-hoc gh plugin flows.
---

# Issue Update Standard

## Fuente de scripts (baseline)
Usar scripts de:
`C:\Users\ifaro\OneDrive\Documentos\02.GitHub_Repository\00. Ai_engineering\03.Scripts\00.agent_tools\01.issue_update`

## Flujo
1. Verificar issue objetivo y cambio exacto.
2. Preparar contenido con plantilla `update_issue_template.md` si aplica.
3. Ejecutar actualización con `update_issue.ps1`.
4. Validar que el cambio quedó reflejado en GitHub.
5. Dejar trazabilidad mínima (owner, acción, evidencia, ETA, resultado).

## Reglas
- No actualizar sin owner único y objetivo concreto.
- No usar plugin como vía principal para esta operación.
- Si hay error de acceso/tooling, registrar incidente y siguiente acción forzada.

## Referencias
- `references/script-inventory.md`
- `references/usage-notes.md`
