# HANDOFFS.md

## Regla

Un handoff solo vale si deja:
- Contexto minimo suficiente
- Estado real
- Bloqueo si existe
- Siguiente paso esperado
- Criterio de cierre

## Evitar

- Handoffs ambiguos
- Transferir trabajo sin decision
- Descargar responsabilidad sin ownership claro

## Protocolo de handoff

### Sandra → Especialista

```markdown
## Handoff desde Sandra

**Contexto:** [Situacion de Ignacio]
**Entregable esperado:** [Que debe producir el especialista]
**Fecha limite:** [Cuando se necesita]
**Prioridad:** P0/P1/P2
**Datos relevantes:** [Rutas a archivos, informacion clave]
```

### Especialista → Sandra

```markdown
## Entrega a Sandra

**Issue:** #[numero]
**Estado:** [Completado/En progreso/Bloqueado]
**Entregable:** [Resumen de lo producido]
**Ruta:** [Donde esta el resultado]
**Decision necesaria:** [Si/Ni - Que necesita decidir Ignacio]
**Siguiente paso:** [Que pasaria despues]
```

## Canales de handoff

1. **GitHub Issues:** Para trabajo estructurado con seguimiento
2. **Mensajes directos (sessions_send):** Para coordinacion tactica urgente
3. **Obsidian:** Para documentacion y memoria compartida
