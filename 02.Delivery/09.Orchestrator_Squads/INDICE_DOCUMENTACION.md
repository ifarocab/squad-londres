# INDICE DE DOCUMENTACION
## Orquestador Multi-Squad

---

## Documentos Disponibles

### 1. README.md
**Tipo**: Documentacion general  
**Contenido**: Vision general del sistema, instalacion basica, uso y mantenimiento  
**Publico**: Todos los usuarios  
**Estado**: Completo

### 2. DOCUMENTACION_TECNICA.md  
**Tipo**: Documentacion tecnica  
**Contenido**: Componentes del sistema, configuracion detallada, flujo de ejecucion, seguridad  
**Publico**: Desarrolladores, DevOps  
**Estado**: Completo

### 3. GUIA_OPERACION.md
**Tipo**: Guia de operacion  
**Contenido**: Instalacion rapida, operacion diaria, troubleshooting, comandos utiles  
**Publico**: Operadores, Administradores  
**Estado**: Completo

---

## Archivos de Configuracion

### config/squads.ini
Configuracion de squads y repositorios

---

## Scripts

### scripts/orchestrator.py
Orquestador principal

### scripts/detect-light.py
Deteccion ligera de issues

### scripts/detect-deep.py
Analisis profundo

### scripts/todo-executor.py
Ejecutor de acciones

### scripts/lib/github_api.py
API de GitHub

---

## Wrappers

### wrappers/run-orchestrator.bat
Ejecutor para Task Scheduler

### wrappers/setup-task-scheduler.bat
Instalador de tarea programada

---

## Fecha de Documentacion
2026-05-05

## Version
1.0
