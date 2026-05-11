"""
Manejo de queue de acciones para el Squad Madrid
"""
import json
import os
from datetime import datetime
from typing import List, Dict, Optional

QUEUE_PATH = os.path.expanduser("~/.openclaw/cron/squad-madrid-queue.json")
REPORTS_PATH = os.path.expanduser("~/.openclaw/cron/squad-madrid-reports")

class QueueManager:
    def __init__(self, queue_path: str = QUEUE_PATH):
        self.queue_path = queue_path
        self._ensure_queue_exists()
    
    def _ensure_queue_exists(self):
        """Asegura que el archivo de queue existe"""
        if not os.path.exists(self.queue_path):
            self.clear()
    
    def read(self) -> Dict:
        """Lee la queue actual"""
        try:
            with open(self.queue_path, 'r', encoding='utf-8') as f:
                return json.load(f)
        except Exception as e:
            print(f"Error leyendo queue: {e}")
            return {"version": 1, "timestamp": "", "actions": []}
    
    def write(self, actions: List[Dict], timestamp: Optional[str] = None):
        """Escribe acciones en la queue"""
        data = {
            "version": 1,
            "timestamp": timestamp or datetime.now().isoformat(),
            "actions": actions
        }
        try:
            with open(self.queue_path, 'w', encoding='utf-8') as f:
                json.dump(data, f, indent=2, ensure_ascii=False)
            return True
        except Exception as e:
            print(f"Error escribiendo queue: {e}")
            return False
    
    def clear(self):
        """Limpia la queue"""
        return self.write([])
    
    def add_action(self, issue: str, owner: str, action: str, reason: str = ""):
        """Añade una acción a la queue"""
        queue = self.read()
        queue["actions"].append({
            "issue": issue,
            "owner": owner,
            "action": action,
            "reason": reason,
            "added_at": datetime.now().isoformat()
        })
        return self.write(queue["actions"])

class ReportManager:
    def __init__(self, reports_dir: str = REPORTS_PATH):
        self.reports_dir = reports_dir
        os.makedirs(reports_dir, exist_ok=True)
    
    def save_daily_report(self, report_data: Dict):
        """Guarda reporte diario"""
        date_str = datetime.now().strftime("%Y-%m-%d")
        filename = f"squad-madrid-daily-report-{date_str}.json"
        filepath = os.path.join(self.reports_dir, filename)
        
        report_data["generated_at"] = datetime.now().isoformat()
        report_data["date"] = date_str
        
        try:
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(report_data, f, indent=2, ensure_ascii=False)
            return filepath
        except Exception as e:
            print(f"Error guardando reporte: {e}")
            return None
    
    def get_latest_report(self) -> Optional[Dict]:
        """Obtiene el reporte más reciente"""
        try:
            files = sorted([f for f in os.listdir(self.reports_dir) if f.endswith('.json')])
            if not files:
                return None
            with open(os.path.join(self.reports_dir, files[-1]), 'r') as f:
                return json.load(f)
        except Exception:
            return None

if __name__ == "__main__":
    # Test
    q = QueueManager()
    print(f"Queue actual: {q.read()}")
