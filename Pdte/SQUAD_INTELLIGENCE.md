# SQUAD_INTELLIGENCE.md

## Objetivo

Optimizar el flujo total del squad, no solo la tarea local.

## Vigilar

- duplicidad
- peloteo
- bloqueos reales
- handoffs pobres
- desalineación
- sobredelegación
- proliferación innecesaria de subagentes

## Agent collaboration rule

Delegar o colaborar cuando:
- otro agente tiene mayor especialización
- la tarea requiere conocimiento que no posee
- el coste de hacerlo solo es mayor
- mejora calidad o velocidad del resultado

Debe:
- enviar contexto mínimo suficiente
- definir objetivo claro
- pedir output accionable

## Ownership

- quien abre una línea de trabajo mantiene ownership
- delegar no transfiere responsabilidad final salvo handoff explícito
- si un subagente falla, el agente padre resuelve o redirige
