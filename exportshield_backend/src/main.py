import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.pollution import router as pollution_router
from src.routes.safety import router as safety_router
from src.routes.workers import router as workers_router
from src.routes.machinery import router as machinery_router
from src.routes.incidents import router as incidents_router
from src.routes.corridors import router as corridors_router
from src.routes.dashboard import router as dashboard_router


app = FastAPI(
    title="MiningMitra Backend API",
    version="1.0.0",
    description="""
    🏭 **MiningMitra Mining Safety & Monitoring System**
    
    A comprehensive backend API for real-time mining operations monitoring, 
    worker safety tracking, equipment management, and incident reporting.
    
    ## Features
    
    * 👷 **Worker Monitoring** - Real-time health vitals and location tracking
    * 🚜 **Machinery Management** - Equipment health, maintenance, and predictive analytics
    * ⚠️ **Incident Reporting** - Safety incident tracking and heatmap visualization
    * 🛣️ **Corridor Monitoring** - Environmental metrics and compliance tracking
    * 📊 **Dashboard Analytics** - Comprehensive statistics and live alerts
    * 🔬 **Pollution Analysis** - Environmental impact assessment
    * 🛡️ **Safety Scoring** - Real-time safety score calculations
    
    ## Quick Start
    
    Visit `/docs` for interactive API documentation and testing.
    """,
    contact={
        "name": "MiningMitra Team",
        "url": "https://miningmitra.vercel.app",
    },
    license_info={
        "name": "MIT",
    }
)

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
    """Root endpoint with API information"""
    return {
        "message": "🏭 MiningMitra Backend API - Running Successfully",
        "version": "1.0.0",
        "status": "operational",
        "documentation": "/docs",
        "redoc": "/redoc",
        "health_check": "/health",
        "api_endpoints": {
            "dashboard": {
                "statistics": "/api/dashboard/statistics",
                "live_alerts": "/api/dashboard/alerts/live",
            },
            "workers": {
                "all": "/api/workers",
                "critical": "/api/workers/critical",
                "by_id": "/api/workers/{id}",
            },
            "machinery": {
                "all": "/api/machinery",
                "critical": "/api/machinery/critical",
                "by_id": "/api/machinery/{id}",
            },
            "incidents": {
                "all": "/api/incidents",
                "active": "/api/incidents/active",
                "critical": "/api/incidents/critical",
                "heatmap": "/api/incidents/heatmap",
                "by_id": "/api/incidents/{id}",
            },
            "corridors": {
                "all": "/api/corridors",
                "metrics": "/api/corridors/metrics/average",
                "by_id": "/api/corridors/{id}",
            },
            "analytics": {
                "pollution": "/api/pollution?depth=100&explosives=50",
                "safety": "/api/safety?temperature=30&vibration=5",
            }
        },
        "demo_info": {
            "total_workers": 8,
            "total_machinery": 6,
            "active_incidents": 4,
            "monitoring_zones": 4,
        }
    }


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
app.include_router(dashboard_router)
app.include_router(workers_router)
app.include_router(machinery_router)
app.include_router(incidents_router)
app.include_router(corridors_router)
app.include_router(pollution_router)
app.include_router(safety_router)
