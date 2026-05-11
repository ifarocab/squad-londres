#!/usr/bin/env python3
import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))

from github_api import GitHubAPI
from queue import QueueManager
from datetime import datetime

def has_single_owner(issue):
    labels = [label['name'] for label in issue.get('labels', [])]
    owners = [l.replace('owner:', '') for l in labels if l.startswith('owner:')]
    if len(owners) == 1:
        return True, owners[0]
    assignees = issue.get('assignees', [])
    if len(assignees) == 1:
        return True, assignees[0]['login']
    return False, ""

def is_blocked(issue):
    labels = [label['name'] for label in issue.get('labels', [])]
    if 'blocked' in labels:
        return True, "Label blocked"
    return False, ""

def can_move_to_in_progress(issue):
    has_owner, owner = has_single_owner(issue)
    if not has_owner:
        return False, "", "Sin owner unico"
    is_block, reason = is_blocked(issue)
    if is_block:
        return False, "", f"Bloqueada: {reason}"
    return True, owner, "Lista para progresar"

def main():
    print(f"[{datetime.now().isoformat()}] detect-light iniciado")
    api = GitHubAPI()
    queue = QueueManager()
    
    print("Consultando issues...")
    backlog = api.get_issues(labels=["backlog"])
    ready = api.get_issues(labels=["ready"])
    all_issues = backlog + ready
    print(f"Total: {len(all_issues)} (backlog: {len(backlog)}, ready: {len(ready)})")
    
    actions = []
    for issue in all_issues[:10]:
        can_move, owner, reason = can_move_to_in_progress(issue)
        if can_move:
            actions.append({
                "issue": f"#{issue['number']}",
                "title": issue['title'][:50],
                "owner": owner,
                "action": "move_to_in_progress",
                "reason": reason
            })
            print(f"  + #{issue['number']}: {owner}")
    
    queue.write(actions)
    print(f"Queue actualizada: {len(actions)} acciones")
    print(f"HEARTBEAT_OK: {len(actions)} issues listas para In Progress")
    return 0

if __name__ == "__main__":
    sys.exit(main())
