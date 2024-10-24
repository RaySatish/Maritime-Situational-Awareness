from dataclasses import dataclass
from typing import List, Dict
import pandas as pd

@dataclass
class MaritimeData:
    vessel_id: str
    vessel_type: str
    coordinates: Dict[str, float]
    speed: float
    heading: float
    timestamp: str
    status: str

class MaritimeDataset:
    def __init__(self):
        self.historical_data = pd.read_csv('data/historical_maritime_data.csv')
        self.vessel_types = pd.read_csv('data/vessel_types.csv')
        self.threat_patterns = pd.read_csv('data/threat_patterns.csv')
