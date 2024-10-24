# tests/test_api.py
from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_get_reports():
    response = client.get("/api/v1/reports")
    assert response.status_code == 200

def test_add_report():
    payload = {
        "coordinates": "13°45'N, 71°23'W",
        "issue": "Detected submarine periscope",
        "rag_context": "Historical context not available"
    }
    response = client.post("/api/v1/reports", json=payload)
    assert response.status_code == 200
