from fastapi import FastAPI
from app.api.telemetry import router as telemetry_router
from app.core.metrics import setup_metrics

app = FastAPI(
    title="Telemetry API",
    description="API for telemetry data and operational monitoring",
    version="1.0.0",
)

setup_metrics(app)

app.include_router(telemetry_router)

@app.get("/")
async def root():
    return {"message": "Welcome to the Telemetry API"}

@app.get("/healthz")
async def health_check():
    return {"status": "ok"}

@app.get("/readyz")
async def readiness_check():
    return {"status": "ready"}
