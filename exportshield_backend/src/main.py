import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.pollution import router as pollution_router
from src.routes.safety import router as safety_router
from src.routes.workers import router as workers_router
from src.routes.machinery import router as machinery_router
from src.routes.incidents import router as incidents_router
from src.routes.corridors import router as corridors_router


app = FastAPI(title="MiningMitra Backend", version="1.0.0")

# CORS Configuration - Allow all development and production origins
allowed_origins = [
    "http://localhost:5173",
    "http://localhost:8080",           # Add port 8080 for Vite
    "http://localhost:3000",
    "http://localhost:5174",
    "http://localhost:8000",
    "http://127.0.0.1:5173",
    "http://127.0.0.1:8080",           # Add 127.0.0.1:8080
    "http://127.0.0.1:3000",
    "http://127.0.0.1:5174",
    "http://127.0.0.1:8000",
    "https://miningmitra.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,     # Specific origins (no "*" with credentials)
    allow_credentials=False,           # Disable credentials for now
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=["*"],
    expose_headers=["Content-Range", "X-Content-Range"],
    max_age=86400,
)


@app.get("/")
def read_root() -> dict:
    return {"message": "MiningMitra Backend Running Successfully"}


@app.get("/health")
def health_check() -> dict:
    """Health check endpoint for monitoring and CORS testing"""
    from datetime import datetime
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "service": "MiningMitra Backend API",
        "endpoints": [
            "/api/workers",
            "/api/machinery",
            "/api/incidents",
            "/api/corridors",
            "/api/pollution",
            "/api/safety",
        ]
    }


# Include all routers
app.include_router(pollution_router)
app.include_router(safety_router)
app.include_router(workers_router)
app.include_router(machinery_router)
app.include_router(incidents_router)
app.include_router(corridors_router)
