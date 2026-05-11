# DOCUMENTACION TECNICA - ORQUESTADOR MULTI-SQUAD

## 1. COMPONENTES DEL SISTEMA

### 1.1 orchestrator.py
Orquestador principal que lee configuracion y ejecuta jobs.

### 1.2 detect-light.py
Deteccion ligera de issues listas para avanzar.

### 1.3 detect-deep.py
Analisis profundo de issues.

### 1.4 todo-executor.py
Ejecutor de acciones pendientes.

### 1.5 github_api.py
Wrapper de API de GitHub.

## 2. CONFIGURACION

Archivo: config/squads.ini

## 3. FLUJO DE EJECUCION

Task Scheduler -> Batch -> Python -> Config -> Scripts -> GitHub

## 4. SEGURIDAD

- Token almacenado en variable de entorno
- No se guarda en archivos
- Acceso solo a repositorios configurados

## 5. MANTENIMIENTO

Ver logs en: logs/cron/

Documentacion tecnica completa.
