# CONTEXT_HYGIENE.md

## Objetivo

Evitar degradación por inflación de contexto, truncation, bootstrap sobredimensionado o duplicidad documental.

## Incidentes a tratar

- `truncating in injected context`
- timeouts donde el contexto sea causa probable
- `AGENTS.md` o bootstrap demasiado largos
- duplicidad entre `AGENTS.md`, `SOUL.md`, `HEARTBEAT.md`, `SELF_IMPROVEMENT.md`
- crecimiento constante de instrucciones con poco impacto real

## Protocolo

1. confirmar patrón o repetición
2. identificar el archivo o bloque responsable
3. clasificar contenido:
   - nuclear
   - operativo
   - de referencia
   - prescindible
4. actuar en este orden:
   - eliminar duplicidad
   - comprimir texto no operativo
   - mover detalle a referencias o skills
   - dividir bootstrap en capas si aporta claridad
5. registrar la mejora si genera aprendizaje
6. elevar a Lucía si afecta a varios agentes o squads

## Regla nuclear

Mantener en bootstrap solo lo que cambia decisiones o evita errores relevantes.

## Límites

No tocar:
- identidad nuclear
- límites de seguridad
- permisos
- contratos críticos
sin governance o confirmación según impacto.
