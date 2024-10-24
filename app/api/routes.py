from fastapi import APIRouter, WebSocket, Depends
from app.services.rag_service import MaritimeRAG
from app.services.alert_service import AlertService
from app.data.maritime_dataset import MaritimeDataset

router = APIRouter()
maritime_rag = MaritimeRAG()
alert_service = AlertService()
dataset = MaritimeDataset()

@router.post("/process_report")
async def process_maritime_report(report: str):
    processed_data = maritime_rag.process_report(report)
    alerts = alert_service.check_threats(processed_data)
    return {"data": processed_data, "alerts": alerts}

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            processed_data = maritime_rag.process_report(data['report'])
            await websocket.send_json(processed_data)
    except WebSocketDisconnect:
        pass