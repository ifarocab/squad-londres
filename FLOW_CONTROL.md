# FLOW_CONTROL.md

## Objetivo

Mantener throughput alto con el menor ruido posible en el Squad Londres.

## Reglas

- No delegar tareas de un paso si resolver directo es mejor
- No crear subagente si no aporta paralelizacion o especializacion real
- No abrir nuevas ramas sin beneficio claro
- Preferir menos nodos y mejor criterio

## Señales de mala eficiencia

- Mas movimiento que avance
- Latencia de coordinacion
- Retrabajo repetido
- Esperas innecesarias

## Flujo de activacion

```
Ignacio → Sandra (preferente)
              ↓
    ¿Tema claro medico/financiero/nutricional?
          │
          Si y urgente ──→ Escalado directo al especialista
          │
          No o dudoso ──→ Sandra gestiona
```

## Regla de manos

Sandra es el punto de entrada por defecto. Los especialistas se activan:
1. Por decision de Sandra
2. Por solicitud directa de Ignacio cuando el tema es claro
3. Por heartbeat detectando necesidad (cita medica proxima, etc.)
