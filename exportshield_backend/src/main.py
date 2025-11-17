import os
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.pollution import router as pollution_router
from src.routes.safety import router as safety_router


app = FastAPI(title="MiningMitra Backend", version="1.0.0")

# CORS Configuration
# Determine allowed origins based on environment
ENVIRONMENT = os.getenv("NODE_ENV", "development")

if ENVIRONMENT == "production":
    # Production: Only allow specific origins
    allowed_origins = [
        "https://miningmitra.vercel.app",
        os.getenv("FRONTEND_URL", "https://miningmitra.vercel.app"),
        # Add your custom domain if you have one
    ]
else:
    # Development: Allow local development servers
    allowed_origins = [
        "http://localhost:5173",           # Vite dev server
        "http://localhost:3000",           # Alternative dev port
        "http://localhost:5174",           # Alternative Vite port
        "http://localhost:8000",           # FastAPI local
        "http://127.0.0.1:5173",
        "http://127.0.0.1:3000",
        "http://127.0.0.1:5174",
        "http://127.0.0.1:8000",
    ]

app.add_middleware(
    CORSMiddleware,
    allow_origins=allowed_origins,
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH", "OPTIONS"],
    allow_headers=[
        "Content-Type",
        "Authorization",
        "X-Requested-With",
        "Accept",
        "Origin",
    ],
    expose_headers=["Content-Range", "X-Content-Range"],
    max_age=86400,  # 24 hours - cache preflight requests
)


@app.get("/")
def read_root() -> dict:
    return {"message": "MiningMitra Backend Running Successfully 🚀"}


@app.get("/health")
def health_check() -> dict:
    """Health check endpoint for monitoring and CORS testing"""
    from datetime import datetime
    return {
        "status": "ok",
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "service": "MiningMitra Backend API",
        "environment": ENVIRONMENT,
    }


app.include_router(pollution_router)
app.include_router(safety_router)
