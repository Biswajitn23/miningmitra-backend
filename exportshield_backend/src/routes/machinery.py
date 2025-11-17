from fastapi import APIRouter, HTTPException
from typing import List, Optional
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/api/machinery", tags=["Machinery"])


# Pydantic models
class MachineryCreate(BaseModel):
    name: str
    type: str
    location: str
    health: Optional[int] = 100
    status: Optional[str] = "operational"
    operating_hours: Optional[int] = 0
    efficiency: Optional[int] = 100
    vibration: Optional[float] = 0.0
    temperature: Optional[float] = 25.0
    next_maintenance: Optional[str] = None
    predicted_failure_risk: Optional[str] = "low"


class Machinery(BaseModel):
    id: str
    name: str
    type: str
    location: str
    health: int
    status: str
    operating_hours: int
    efficiency: int
    vibration: float
    temperature: float
    next_maintenance: str
    predicted_failure_risk: str
    created_at: str
    updated_at: str


# Mock data
MOCK_MACHINERY = [
    {
        "id": "1",
        "name": "Excavator 1",
        "type": "Excavator",
        "location": "Zone A",
        "health": 85,
        "status": "operational",
        "operating_hours": 1200,
        "efficiency": 92,
        "vibration": 3.2,
        "temperature": 65.0,
        "next_maintenance": "2025-12-01",
        "predicted_failure_risk": "low",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "2",
        "name": "Drill Machine 2",
        "type": "Drill",
        "location": "Zone B",
        "health": 60,
        "status": "maintenance_required",
        "operating_hours": 2500,
        "efficiency": 75,
        "vibration": 8.5,
        "temperature": 85.0,
        "next_maintenance": "2025-11-20",
        "predicted_failure_risk": "high",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "3",
        "name": "Loader 3",
        "type": "Loader",
        "location": "Zone C",
        "health": 95,
        "status": "operational",
        "operating_hours": 500,
        "efficiency": 98,
        "vibration": 2.1,
        "temperature": 55.0,
        "next_maintenance": "2026-01-15",
        "predicted_failure_risk": "low",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
]


@router.get("/", response_model=List[Machinery])
def get_all_machinery():
    """Get all machinery"""
    return MOCK_MACHINERY


@router.get("/critical", response_model=List[Machinery])
def get_critical_machinery():
    """Get machinery that requires maintenance or has high failure risk"""
    return [
        m for m in MOCK_MACHINERY 
        if m["status"] == "maintenance_required" or m["predicted_failure_risk"] == "high"
    ]


@router.get("/{machinery_id}", response_model=Machinery)
def get_machinery(machinery_id: str):
    """Get specific machinery by ID"""
    machinery = next((m for m in MOCK_MACHINERY if m["id"] == machinery_id), None)
    if not machinery:
        raise HTTPException(status_code=404, detail="Machinery not found")
    return machinery


@router.post("/", response_model=Machinery, status_code=201)
def create_machinery(machinery: MachineryCreate):
    """Create new machinery entry"""
    new_machinery = {
        "id": str(len(MOCK_MACHINERY) + 1),
        **machinery.dict(),
        "next_maintenance": machinery.next_maintenance or "2025-12-31",
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_MACHINERY.append(new_machinery)
    return new_machinery


@router.put("/{machinery_id}", response_model=Machinery)
def update_machinery(machinery_id: str, machinery: MachineryCreate):
    """Update existing machinery"""
    machinery_index = next((i for i, m in enumerate(MOCK_MACHINERY) if m["id"] == machinery_id), None)
    if machinery_index is None:
        raise HTTPException(status_code=404, detail="Machinery not found")
    
    updated_machinery = {
        "id": machinery_id,
        **machinery.dict(),
        "next_maintenance": machinery.next_maintenance or MOCK_MACHINERY[machinery_index]["next_maintenance"],
        "created_at": MOCK_MACHINERY[machinery_index]["created_at"],
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_MACHINERY[machinery_index] = updated_machinery
    return updated_machinery


@router.delete("/{machinery_id}")
def delete_machinery(machinery_id: str):
    """Delete machinery"""
    machinery_index = next((i for i, m in enumerate(MOCK_MACHINERY) if m["id"] == machinery_id), None)
    if machinery_index is None:
        raise HTTPException(status_code=404, detail="Machinery not found")
    
    MOCK_MACHINERY.pop(machinery_index)
    return {"message": "Machinery deleted", "id": machinery_id}
