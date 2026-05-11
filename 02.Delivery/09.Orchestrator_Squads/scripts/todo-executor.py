#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from github_api import GitHubAPI
from queue import QueueManager
from datetime import datetime

def move_to_in_progress(issue_number, api):
    """Mueve una issue a In Progress usando GitHub Projects API"""
    # Por ahora, actualizamos labels (backlog -> in-progress)
    # La integracion completa con GitHub Projects requiere GraphQL
    
    issue = api.get_issue(int(issue_number.replace('#', '')))
    if not issue:
        return False, "No se pudo obtener la issue"
    
    current_labels = [l['name'] for l in issue['labels']]
    
    # Quitar backlog, anadir in-progress
    new_labels = [l for l in current_labels if l != 'backlog']
    if 'in-progress' not in new_labels:
        new_labels.append('in-progress')
    
    success = api.update_issue_labels(int(issue_number.replace('#', '')), new_labels)
    
    if success:
        return True, f"Labels actualizados: {new_labels}"
    else:
        return False, "Error actualizando labels"

def main():
    print(f"[{datetime.now().isoformat()}] todo-executor iniciado")
    
    api = GitHubAPI()
    queue = QueueManager()
    
    # Leer queue
    data = queue.read()
    actions = data.get('actions', [])
    
    if not actions:
        print("Queue vacia. Nada que ejecutar.")
        print("HEARTBEAT_OK: 0 acciones")
        return 0
    
    print(f"Acciones pendientes: {len(actions)}")
    
    executed = 0
    errors = 0
    
    for action in actions[:5]:  # Max 5 acciones por ciclo
        issue = action.get('issue')
        owner = action.get('owner')
        action_type = action.get('action')
        
        print(f"Procesando {issue} (owner: {owner}, action: {action_type})")
        
        if action_type == 'move_to_in_progress':
            success, msg = move_to_in_progress(issue, api)
            if success:
                print(f"  OK: {msg}")
                executed += 1
            else:
                print(f"  ERROR: {msg}")
                errors += 1
        else:
            print(f"  SKIP: Accion no soportada: {action_type}")
    
    # Limpiar queue
    queue.clear()
    print(f"Queue limpiada. Ejecutadas: {executed}, Errores: {errors}")
    print(f"HEARTBEAT_OK: {executed} ejecutadas, {errors} errores")
    return 0

if __name__ == "__main__":
    sys.exit(main())
