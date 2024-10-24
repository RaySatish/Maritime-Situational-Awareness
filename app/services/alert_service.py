from typing import List, Dict
from fastapi import WebSocket
import numpy as np
from datetime import datetime

class AlertService:
    def __init__(self):
        self.threat_threshold = 0.75
        self.alert_history = []
        
    def analyze_threat(self, vessel_data: Dict) -> Dict:
        threat_score = self._calculate_threat_score(vessel_data)
        alert = None
        
        if threat_score > self.threat_threshold:
            alert = {
                "id": str(datetime.now().timestamp()),
                "level": "high",
                "message": f"Potential threat detected: {vessel_data.get('vessel_id')}",
                "score": threat_score,
                "timestamp": datetime.now().isoformat(),
                "coordinates": vessel_data.get('coordinates')
            }
            self.alert_history.append(alert)
        return alert
    
    def _calculate_threat_score(self, vessel_data: Dict) -> float:
        # Implement threat scoring logic
        factors = [
            self._check_speed_anomaly(vessel_data),
            self._check_restricted_zone(vessel_data),
            self._check_course_changes(vessel_data)
        ]
        return np.mean(factors)

async def send_alert_message(message: str, clients: List[WebSocket]):
    for client in clients:
        try:
            await client.send_json({
                "type": "alert",
                "data": message
            })
        except Exception:
            continue

def generate_alert_message(report_data: dict) -> str:
    return {
        "message": f"Alert: Issue detected at {report_data['coordinates']}",
        "details": report_data['issue'],
        "timestamp": datetime.now().isoformat()
    }
