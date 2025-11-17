from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/api/workers", tags=["Workers"])


# Pydantic models for request/response
class WorkerCreate(BaseModel):
    name: str
    role: str
    zone: str
    latitude: float
    longitude: float
    heart_rate: Optional[int] = None
    temperature: Optional[float] = None
    oxygen_level: Optional[int] = None
    fatigue_level: Optional[str] = "low"
    status: Optional[str] = "active"


class Worker(BaseModel):
    id: str
    name: str
    role: str
    zone: str
    latitude: float
    longitude: float
    heart_rate: int
    temperature: float
    oxygen_level: int
    fatigue_level: str
    status: str
    created_at: str
    updated_at: str


# Mock data - Replace with database queries
MOCK_WORKERS = [
    {
        "id": "1",
        "name": "John Doe",
        "role": "Miner",
        "zone": "Zone A",
        "latitude": 23.5820,
        "longitude": 87.2718,
        "heart_rate": 75,
        "temperature": 37.2,
        "oxygen_level": 98,
        "fatigue_level": "low",
        "status": "active",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "2",
        "name": "Jane Smith",
        "role": "Engineer",
        "zone": "Zone B",
        "latitude": 23.5825,
        "longitude": 87.2720,
        "heart_rate": 82,
        "temperature": 37.8,
        "oxygen_level": 95,
        "fatigue_level": "medium",
        "status": "active",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "3",
        "name": "Mike Johnson",
        "role": "Supervisor",
        "zone": "Zone A",
        "latitude": 23.5815,
        "longitude": 87.2715,
        "heart_rate": 120,
        "temperature": 38.5,
        "oxygen_level": 88,
        "fatigue_level": "high",
        "status": "critical",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
]


@router.get("/", response_model=List[Worker])
def get_all_workers():
    """Get all workers"""
    return MOCK_WORKERS


@router.get("/critical", response_model=List[Worker])
def get_critical_workers():
    """Get workers with critical health status"""
    return [w for w in MOCK_WORKERS if w["status"] == "critical" or w["fatigue_level"] == "high"]


@router.get("/{worker_id}", response_model=Worker)
def get_worker(worker_id: str):
    """Get a specific worker by ID"""
    worker = next((w for w in MOCK_WORKERS if w["id"] == worker_id), None)
    if not worker:
        raise HTTPException(status_code=404, detail="Worker not found")
    return worker


@router.post("/", response_model=Worker, status_code=201)
def create_worker(worker: WorkerCreate):
    """Create a new worker"""
    new_worker = {
        "id": str(len(MOCK_WORKERS) + 1),
        **worker.dict(),
        "heart_rate": worker.heart_rate or 75,
        "temperature": worker.temperature or 37.0,
        "oxygen_level": worker.oxygen_level or 98,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_WORKERS.append(new_worker)
    return new_worker


@router.put("/{worker_id}", response_model=Worker)
def update_worker(worker_id: str, worker: WorkerCreate):
    """Update an existing worker"""
    worker_index = next((i for i, w in enumerate(MOCK_WORKERS) if w["id"] == worker_id), None)
    if worker_index is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    
    updated_worker = {
        "id": worker_id,
        **worker.dict(),
        "heart_rate": worker.heart_rate or MOCK_WORKERS[worker_index]["heart_rate"],
        "temperature": worker.temperature or MOCK_WORKERS[worker_index]["temperature"],
        "oxygen_level": worker.oxygen_level or MOCK_WORKERS[worker_index]["oxygen_level"],
        "created_at": MOCK_WORKERS[worker_index]["created_at"],
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_WORKERS[worker_index] = updated_worker
    return updated_worker


@router.delete("/{worker_id}")
def delete_worker(worker_id: str):
    """Delete a worker"""
    worker_index = next((i for i, w in enumerate(MOCK_WORKERS) if w["id"] == worker_id), None)
    if worker_index is None:
        raise HTTPException(status_code=404, detail="Worker not found")
    
    MOCK_WORKERS.pop(worker_index)
    return {"message": "Worker deleted", "id": worker_id}
