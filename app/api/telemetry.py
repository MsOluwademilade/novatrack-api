from fastapi import APIRouter
from app.models.telemetry import TelemetryIn
from app.core.metrics import telemetry_metric

router = APIRouter()

telemetry_data = []

@router.get("/telemetry")
async def get_telemetry():
    return telemetry_data

@router.post("/telemetry")
async def post_telemetry(data: TelemetryIn):
    telemetry_data.append(data)
    telemetry_metric.inc()  
    return {"status": "data received"}
