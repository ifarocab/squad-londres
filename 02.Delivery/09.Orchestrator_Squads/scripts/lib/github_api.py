"""
GitHub API wrapper para operaciones del Squad Madrid
"""
import os
import json
import urllib.request
import urllib.error
from typing import List, Dict, Optional, Any

class GitHubAPI:
    def __init__(self, token: Optional[str] = None, repo: str = "ifarocab/Exis"):
        self.token = token or self._get_token()
        self.repo = repo
        self.base_url = "https://api.github.com"
        self.headers = {
            "Authorization": f"token {self.token}",
            "Accept": "application/vnd.github.v3+json",
            "User-Agent": "SquadMadrid-Orquestador"
        }
    
    def _get_token(self) -> str:
        """Obtiene token de GH_TOKEN.txt o variable de entorno"""
        token_path = os.path.expanduser("~/.openclaw/workspaces/Squad_Madrid/workspace-ToniSanz/GH_TOKEN.txt")
        if os.path.exists(token_path):
            with open(token_path, 'r') as f:
                return f.read().strip()
        return os.environ.get('GITHUB_TOKEN', '')
    
    def _request(self, endpoint: str, method: str = "GET", data: Optional[Dict] = None) -> Any:
        """Hace petición a GitHub API"""
        url = f"{self.base_url}{endpoint}"
        req = urllib.request.Request(url, headers=self.headers, method=method)
        
        if data:
            req.add_header('Content-Type', 'application/json')
            req.data = json.dumps(data).encode('utf-8')
        
        try:
            with urllib.request.urlopen(req, timeout=30) as response:
                return json.loads(response.read().decode('utf-8'))
        except urllib.error.HTTPError as e:
            print(f"Error HTTP {e.code}: {e.reason}")
            return None
        except Exception as e:
            print(f"Error: {e}")
            return None
    
    def get_issues(self, state: str = "open", labels: Optional[List[str]] = None, per_page: int = 100) -> List[Dict]:
        """Obtiene issues del repo"""
        endpoint = f"/repos/{self.repo}/issues?state={state}&per_page={per_page}"
        if labels:
            endpoint += f"&labels={','.join(labels)}"
        
        issues = self._request(endpoint)
        return issues if issues else []
    
    def get_issue(self, issue_number: int) -> Optional[Dict]:
        """Obtiene una issue específica"""
        return self._request(f"/repos/{self.repo}/issues/{issue_number}")
    
    def get_project_items(self, project_number: int) -> List[Dict]:
        """Obtiene items de un proyecto (requiere GraphQL para campos custom)"""
        # Para campos custom como Status, necesitamos GraphQL
        # Esto es un placeholder - la implementación real usaría la API v4
        return []
    
    def update_issue_labels(self, issue_number: int, labels: List[str]) -> bool:
        """Actualiza labels de una issue"""
        result = self._request(
            f"/repos/{self.repo}/issues/{issue_number}",
            method="PATCH",
            data={"labels": labels}
        )
        return result is not None

if __name__ == "__main__":
    # Test
    api = GitHubAPI()
    issues = api.get_issues(labels=["backlog"])
    print(f"Issues en backlog: {len(issues)}")
