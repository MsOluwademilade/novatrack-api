from pydantic import BaseModel
from typing import Optional

class Telemetry(BaseModel):
    source: str
    timestamp: str
    temperature_c: float
    humidity_pct: float
    status: Optional[str] = "ok"

class TelemetryIn(BaseModel):
    source: str
    timestamp: str
    temperature_c: float
    humidity_pct: float
    status: Optional[str] = "ok"