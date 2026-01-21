from fastapi import FastAPI, Response, Request
from prometheus_client import Counter, Histogram, Gauge, generate_latest, CONTENT_TYPE_LATEST, REGISTRY
import time

# Metrics
telemetry_metric = Counter(
    "telemetry_records_total",
    "Total number of telemetry records received"
)

request_duration = Histogram(
    "http_request_duration_seconds",
    "HTTP request duration in seconds",
    ["method", "endpoint", "status"]
)

active_requests = Gauge(
    "active_requests",
    "Number of requests currently being processed"
)

def setup_metrics(app: FastAPI) -> None:
    # Middleware to track request metrics
    @app.middleware("http")
    async def track_requests(request: Request, call_next):
        if request.url.path == "/metrics":
            return await call_next(request)
        
        active_requests.inc()
        start_time = time.time()
        
        response = await call_next(request)
        
        duration = time.time() - start_time
        request_duration.labels(
            method=request.method,
            endpoint=request.url.path,
            status=response.status_code
        ).observe(duration)
        
        active_requests.dec()
        return response

    @app.get("/metrics")
    def metrics():
        return Response(
            content=generate_latest(REGISTRY),
            media_type=CONTENT_TYPE_LATEST,
        )

    @app.post("/telemetry")
    async def receive_telemetry(data: dict):
        telemetry_metric.inc()
        return {"message": "Telemetry received successfully"}
