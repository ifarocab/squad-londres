# FLOW_CONTROL.md

## Objetivo

Mantener throughput alto con el menor ruido posible.

## Reglas

- no delegar tareas de un paso si resolver directo es mejor
- no crear subagente si no aporta paralelización o especialización real
- no abrir nuevas ramas sin beneficio claro
- preferir menos nodos y mejor criterio

## Señales de mala eficiencia

- más movimiento que avance
- latencia de coordinación
- retrabajo repetido
- esperas innecesarias
