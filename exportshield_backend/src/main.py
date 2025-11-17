from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from src.routes.pollution import router as pollution_router
from src.routes.safety import router as safety_router


app = FastAPI(title="MiningMitra Backend", version="1.0.0")

# Enable CORS for all origins
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def read_root() -> dict:
    return {"message": "MiningMitra Backend Running Successfully 🚀"}


app.include_router(pollution_router)
app.include_router(safety_router)
