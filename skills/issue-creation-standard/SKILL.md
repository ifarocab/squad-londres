---
name: issue-creation-standard
version: "1.1"
description: Crear issues normalizadas del squad con calidad operativa y de producto. Usar cuando Marta u otro agente necesite dar de alta una issue nueva (feature/story/task/subtask), validar completitud mínima, evitar duplicados y dejar trazabilidad lista para ejecución.
---

# Issue Creation Standard v1.1

Crear toda issue usando este estándar del squad.

## ⚠️ REGLA MANDATORY DEL SQUAD

**Toda issue DEBE incluir el label product-board**

Sin este label, la issue NO aparecerá en el Product Board y NO será gestionada por el squad.

## Pasos

1. Buscar duplicidad antes de crear.
2. Definir jerarquía explícita: feature|epic y story|task|subtask.
3. Completar campos obligatorios.
4. Añadir SIEMPRE label product-board (MANDATORY).
5. Validar reglas de calidad.
6. Crear la issue.
7. Confirmar evidencias de creación.

## Campos obligatorios

- Título normalizado y accionable.
- Prioridad P0..P5.
- Feature/Epic.
- Tipo: story|task|subtask.
- Estado inicial: backlog|ready|in-progress.
- Owner real.
- Impacto.
- Dependencias explícitas.
- Entregable mínimo esperado.
- Criterios de aceptación.
- Label product-board (MANDATORY).

## Labels obligatorios

1. product-board - Mandatory para visibilidad en dashboard
2. type-feature|bug|task|story|improvement - Tipo de issue
3. P0-critical|P1-high|P2-medium|P3-low - Prioridad
4. owner-{nombre} - Responsable

## Reglas de calidad

- No crear issue sin label product-board.
- No crear issue con owner teórico.
- No dejar dependencias implícitas.
- No permitir título genérico.

## Gestión de errores

ERROR_MISSING_PRODUCT_BOARD_LABEL: Obligatory label product-board is required

## Referencias

- Política del squad: 02.references/ISSUE_LABEL_POLICY.md
