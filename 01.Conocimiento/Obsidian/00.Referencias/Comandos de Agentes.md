# Comandos de Agentes

## Crear sesión a un agente

```powershell
openclaw agent --agent <nombre_agente> --session-id main --message "init"
```

### Uso
- Reemplazar `<nombre_agente>` con el nombre del agente deseado
- El flag `--session-id main` crea/usa la sesión principal
- El mensaje `"init"` inicializa la conversación

### Ejemplo
```powershell
openclaw agent --agent sandra-provencio --session-id main --message "init"
```

---
Guardado para uso rápido cuando Iñaki solicite crear sesiones de agentes
