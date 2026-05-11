# CONTEXT_HYGIENE.md

## Gestion de contexto

### Limites de bootstrap

- AGENTS.md: Max 5000 caracteres
- SOUL.md: Max 5000 caracteres
- TOOLS.md: Max 5000 caracteres
- Total bootstrap: Max 30000 caracteres

### Cuando compactar

- Truncamiento detectado (> 60%)
- Bootstrap lento (> 5s)
- Memoria operativa > 50 entradas

### Estrategia de compactacion

1. Revisar memory/YYYY-MM-DD.md antiguos (> 30 dias)
2. Promover a MEMORY.md solo lo duradero
3. Archivar en memory/memory_archive/
4. Actualizar SELF_IMPROVEMENT.md con aprendizajes

## Trazabilidad

- Cada decision en governance-decisions.md
- Cada mejora en governance-queue.md
- Cada sesion relevante resume en MEMORY.md
