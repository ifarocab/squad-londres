#!/usr/bin/env python3
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'lib'))
from github_api import GitHubAPI
from queue import ReportManager
from datetime import datetime

def analyze_issue(issue):
    labels = [l['name'] for l in issue.get('labels', [])]
    updated = datetime.fromisoformat(issue['updated_at'].replace('Z', '+00:00'))
    days = (datetime.now(updated.tzinfo) - updated).days
    owners = [l for l in labels if l.startswith('owner:')]
    has_owner = len(owners) == 1 or len(issue.get('assignees', [])) == 1
    is_blocked = 'blocked' in labels
    
    rec = "READY" if has_owner and not is_blocked else "NEEDS_ATTENTION"
    if days > 7: rec = "STALE"
    if is_blocked: rec = "BLOCKED"
    if not has_owner: rec = "NO_OWNER"
    
    return {
        "number": issue['number'],
        "title": issue['title'][:60],
        "days_stale": days,
        "has_owner": has_owner,
        "is_blocked": is_blocked,
        "recommendation": rec
    }

def main():
    print(f"[{datetime.now().isoformat()}] detect-deep iniciado")
    api = GitHubAPI()
    reports = ReportManager()
    
    issues = api.get_issues(per_page=100)
    analyzed = [analyze_issue(i) for i in issues]
    
    summary = {
        "total": len(issues),
        "ready": sum(1 for a in analyzed if a['recommendation'] == 'READY'),
        "blocked": sum(1 for a in analyzed if a['is_blocked']),
        "stale": sum(1 for a in analyzed if a['days_stale'] > 7),
        "no_owner": sum(1 for a in analyzed if not a['has_owner'])
    }
    
    report = {"summary": summary, "issues": analyzed, "timestamp": datetime.now().isoformat()}
    filepath = reports.save_daily_report(report)
    
    print(f"Reporte: {filepath}")
    print(f"Resumen: {summary['ready']} ready, {summary['blocked']} blocked, {summary['stale']} stale")
    print("HEARTBEAT_OK")
    return 0

if __name__ == "__main__":
    sys.exit(main())
