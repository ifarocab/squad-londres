# Policy_Workspace.md

## Estructura de Directorios

Documento de politica para workspaces de agentes OpenClaw.

## 00. Raiz del Workspace

### Directorios de Sistema
- .clawhub/ - Metadatos de ClawHub
- .openclaw/ - Configuracion local

### Directorios Operativos
- memory/ - Memoria operativa
- skills/ - Skills locales

## 01. 00.Agents - Identidad del Agente

00.Agents/
    00.Backup/   - Copia seguridad de definición de agente 
    01.avatars/  - Directorio del avatar principal.
         00.Avatares/ - Set de avatares a poder usar.
	   01.Comunes/  - Avatares junto con Squad o usuario.
    02.subagents/ - Definición de subajentes

## 02. 01.Governance – Gobernanza del agente

01.Governance/
    00.Policies/ - Politicas del agente
    01.contracts/ - Contratos del agente con otros agentes
    02.references/ - Referencias
    03.templates/   - Plantillas para reutilizar

## 03. 02.Delivery - Entrega y Ejecucion

02.Delivery/
    00.run/      - Ejecución de actividades o programas. 
    01.runbooks/ - Programas o scripts de funcionalidades.
    02.tmp/      - Ficheros temporales del agente.
    03.Download/ - Descarga de ficheros.
    04.Dominios/  - Directorio para información, datos, procedimientos o actividad específica del agente. Ejm. 04.Dominios/00.Seleccion y dentro documentos de análisis de selección de un agente de selección de personal
    05.Entregables/ - Entregables o documentos finales (informes,…)

## 04. memory - Memoria Operativa

memory/
    .dreams/
    dreaming/
    memory_archive/
    heartbeat-state.json

## 05. skills - Skills Locales

skills/
    [nombre-skill]/
