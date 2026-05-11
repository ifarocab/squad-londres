# Collaboration (canal interno del squad)

Este directorio registra propuestas de mejora/colaboración que **cumplen metodología de gobierno**.

## Flujo
1. Registrar propuesta en `requests.jsonl` usando `request-template.json`.
2. Validar criterios de gobierno (scope, impacto, owner, evidencia, ETA, RACI mínimo).
3. Si cumple, registrar decisión en `decisions.jsonl` usando `decision-template.json`.
4. Hacer seguimiento en cada ciclo hasta cierre.

## Regla
- Si no cumple criterios de gobierno, no pasa a decisión: queda en `open` con faltantes explícitos.
- Si cumple, debe tener owner y fecha objetivo.
