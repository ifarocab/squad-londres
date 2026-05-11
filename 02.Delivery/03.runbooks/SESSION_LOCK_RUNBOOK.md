# Runbook: Session & Lock Discipline

## Pre-Lock Checklist
- [ ] Identificar recurso a bloquear
- [ ] Verificar que no hay LLM en ejecución
- [ ] Estimar tiempo de operación (<5s objetivo)

## Durante Lock
- [ ] NO llamar a LLM bajo lock
- [ ] Operaciones atómicas únicamente
- [ ] Medir tiempo de lock

## Post-Lock
- [ ] Liberar lock inmediatamente
- [ ] Persistir estado (máx 2 veces)
- [ ] Registrar métricas si aplica

## Validación
- Lock duration: __ seconds (objetivo <5s)
- LLM calls under lock: 0
- Persistencias: __ (máx 2)

## Referencias
- Política: [../00.policies/SESSION_LOCK_POLICY.md](../00.policies/SESSION_LOCK_POLICY.md)
