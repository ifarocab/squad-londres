# Normativa de nomenclatura de sesiones en OpenClaw

## Objetivo

Definir una convención simple, estable y trazable para nombrar sesiones de los agentes en OpenClaw, distinguiendo entre:

* sesión principal persistente
* sesiones de trabajo temático
* sesiones operativas
* sesiones de diagnóstico
* sesiones temporales
* sesiones de automatismos

Esta norma busca:

* mejorar la trazabilidad
* facilitar la lectura de sesiones activas e históricas
* reducir confusión entre sesiones de distinto propósito
* facilitar mantenimiento, depuración y gobierno operativo

\---

## Principios generales

### 1\. La sesión principal estándar se llama siempre `main`

* `main` es la sesión persistente principal del agente.
* No debe sustituirse por alias arbitrarios.
* No deben crearse variantes como:

  * `main2`
  * `principal`
  * `base`
  * `home`

### 2\. Usar nombres semánticos y cortos

Los nombres deben indicar claramente el propósito de la sesión.

### 3\. Formato obligatorio

* minúsculas
* sin espacios
* palabras separadas por `-`
* sin caracteres especiales innecesarios
* nombre breve, claro y estable

### 4\. No usar nombres ambiguos

No se permiten nombres como:

* `prueba`
* `test`
* `nuevo`
* `cosas`
* `tmp2`
* `sesion1`

\---

## Catálogo oficial de nombres

### `main`

Sesión principal persistente del agente.

**Uso**

* conversación principal estable
* interlocución habitual con el usuario
* continuidad operativa normal del agente

**Ejemplos**

* `main`

\---

### `wrk-<tema>`

Sesión de trabajo temático con cierta continuidad.

**Uso**

* trabajo activo sobre un tema concreto
* tareas o líneas de trabajo que conviene separar de `main`
* asuntos que pueden durar varios días o sesiones

**Ejemplos**

* `wrk-openclaw-logging`
* `wrk-linkedin-candidaturas`
* `wrk-obsidian-gobierno`

\---

### `ops-<tema>`

Sesión operativa o de coordinación.

**Uso**

* coordinación entre agentes
* operación del squad
* gestión de flujos, handoffs, bloqueos o gobierno operativo

**Ejemplos**

* `ops-squad-madrid`
* `ops-release-readiness`
* `ops-backlog-flujo`

\---

### `diag-<tema>`

Sesión de diagnóstico o troubleshooting.

**Uso**

* análisis de incidencias
* problemas de configuración
* problemas de routing, canales, sesiones o herramientas
* depuración técnica aislada

**Ejemplos**

* `diag-telegram-routing`
* `diag-openclaw-latencia`
* `diag-session-reset`

\---

### `tmp-<tema>`

Sesión temporal o efímera.

**Uso**

* pruebas rápidas
* validaciones puntuales
* experimentación no persistente
* tareas que no deben contaminar `main`

**Ejemplos**

* `tmp-prompt-test`
* `tmp-telegram-prueba`
* `tmp-json-check`

**Regla**

* `tmp-\\\*` no debe convertirse en sesión estructural.
* Si el tema gana continuidad, debe migrarse a `wrk-\\\*`, `ops-\\\*` o `diag-\\\*`.

\---

### `cron-<tema>`

Sesión específica para automatismos recurrentes.

**Uso**

* tareas programadas
* crons persistentes
* revisiones periódicas identificables

**Ejemplos**

* `cron-daily-briefing`
* `cron-weekly-review`
* `cron-followup-check`

\---

### `hook-<tema>`

Sesión reservada para hooks o integraciones técnicas, si aplica.

**Uso**

* eventos técnicos
* llamadas automáticas externas
* flujos iniciados por integraciones

**Ejemplos**

* `hook-session-health`
* `hook-webchat-sync`
* `hook-agent-activation`

\---

## Reglas de ciclo de vida

### `main`

* es la sesión principal estable
* no se elimina salvo decisión expresa
* debe mantenerse limpia y útil

### `wrk-\\\*`

* vive mientras el trabajo siga abierto
* puede mantenerse varios días o semanas si el tema lo justifica

### `ops-\\\*`

* vive mientras exista la necesidad operativa
* debe cerrarse o dejar de usarse cuando la operación cambie

### `diag-\\\*`

* debe usarse solo mientras exista la incidencia
* una vez resuelto el problema, no debe reutilizarse para otro distinto

### `tmp-\\\*`

* se considera desechable
* no debe usarse para trabajo relevante o persistente

### `cron-\\\*`

* puede mantenerse estable a largo plazo
* debe existir solo si el automatismo necesita identidad propia de sesión

### `hook-\\\*`

* debe reservarse para integraciones
* no debe usarse para trabajo manual

\---

## Reglas de uso

### 1\. Un propósito por sesión

Cada sesión debe tener un propósito claro y único.

### 2\. No mezclar categorías

* no usar `diag-\\\*` para trabajo normal
* no usar `tmp-\\\*` para operación real
* no usar `ops-\\\*` como sustituto genérico de `main`

### 3\. No crear sesiones libres sin convención

Toda sesión nueva debe encajar en una categoría oficial.

### 4\. Reutilizar con criterio

* reutilizar una sesión si el tema sigue siendo el mismo
* crear una nueva si el propósito cambia de forma clara

### 5\. Evitar proliferación innecesaria

No abrir sesiones específicas si el trabajo cabe razonablemente en `main`.

\---

## Ejemplos correctos

* `main`
* `wrk-openclaw-observabilidad`
* `wrk-exis-requisitos`
* `ops-squad-madrid`
* `diag-telegram-routing`
* `tmp-prompt-mail`
* `cron-daily-briefing`
* `hook-session-health`

## Ejemplos incorrectos

* `Prueba`
* `MAIN`
* `session nueva`
* `cosas`
* `test2`
* `principal`
* `main-final`
* `tmp`
* `diagnostico`
* `nuevo-intento`

\_\_\_

La regla central es:

**cada agente tiene una única sesión principal llamada `main`, y cualquier otra sesión debe pertenecer a una categoría oficial con nombre claro, corto y semántico.**

