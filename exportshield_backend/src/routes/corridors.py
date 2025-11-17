from fastapi import APIRouter, HTTPException
from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/api/corridors", tags=["Corridors"])


# Pydantic models
class CorridorCreate(BaseModel):
    name: str
    from_location: str
    to_location: str
    score: Optional[int] = 50
    risk_level: Optional[str] = "medium"
    pollution: Optional[int] = 50
    green_cover: Optional[int] = 10
    temperature: Optional[float] = 25.0
    traffic: Optional[int] = 50
    compliance: Optional[int] = 80
    latitude: float
    longitude: float
    route_end_lat: float
    route_end_lng: float


class Corridor(BaseModel):
    id: str
    name: str
    from_location: str
    to_location: str
    score: int
    risk_level: str
    pollution: int
    green_cover: int
    temperature: float
    traffic: int
    compliance: int
    latitude: float
    longitude: float
    route_end_lat: float
    route_end_lng: float
    created_at: str
    updated_at: str


# Mock data
MOCK_CORRIDORS = [
    {
        "id": "1",
        "name": "Main Tunnel",
        "from_location": "Entrance A",
        "to_location": "Zone B",
        "score": 75,
        "risk_level": "medium",
        "pollution": 45,
        "green_cover": 20,
        "temperature": 28.0,
        "traffic": 60,
        "compliance": 85,
        "latitude": 23.5820,
        "longitude": 87.2718,
        "route_end_lat": 23.5830,
        "route_end_lng": 87.2730,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "2",
        "name": "North Passage",
        "from_location": "Zone B",
        "to_location": "Zone C",
        "score": 85,
        "risk_level": "low",
        "pollution": 30,
        "green_cover": 35,
        "temperature": 25.0,
        "traffic": 40,
        "compliance": 92,
        "latitude": 23.5830,
        "longitude": 87.2730,
        "route_end_lat": 23.5840,
        "route_end_lng": 87.2745,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "3",
        "name": "South Access Route",
        "from_location": "Entrance B",
        "to_location": "Zone A",
        "score": 55,
        "risk_level": "high",
        "pollution": 70,
        "green_cover": 8,
        "temperature": 32.0,
        "traffic": 85,
        "compliance": 65,
        "latitude": 23.5810,
        "longitude": 87.2710,
        "route_end_lat": 23.5820,
        "route_end_lng": 87.2718,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "4",
        "name": "Emergency Exit Tunnel",
        "from_location": "Zone C",
        "to_location": "Exit Point",
        "score": 90,
        "risk_level": "low",
        "pollution": 20,
        "green_cover": 45,
        "temperature": 23.0,
        "traffic": 15,
        "compliance": 98,
        "latitude": 23.5840,
        "longitude": 87.2745,
        "route_end_lat": 23.5850,
        "route_end_lng": 87.2755,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
]


@router.get("/", response_model=List[Corridor])
def get_all_corridors():
    """Get all corridors"""
    return MOCK_CORRIDORS


@router.get("/metrics/average")
def get_average_metrics() -> Dict[str, float]:
    """Get average metrics across all corridors"""
    if not MOCK_CORRIDORS:
        return {
            "pollution": 0,
            "greenCover": 0,
            "temperature": 0,
            "traffic": 0,
            "compliance": 0,
        }
    
    total = len(MOCK_CORRIDORS)
    return {
        "pollution": sum(c["pollution"] for c in MOCK_CORRIDORS) / total,
        "greenCover": sum(c["green_cover"] for c in MOCK_CORRIDORS) / total,
        "temperature": sum(c["temperature"] for c in MOCK_CORRIDORS) / total,
        "traffic": sum(c["traffic"] for c in MOCK_CORRIDORS) / total,
        "compliance": sum(c["compliance"] for c in MOCK_CORRIDORS) / total,
    }


@router.get("/{corridor_id}", response_model=Corridor)
def get_corridor(corridor_id: str):
    """Get specific corridor by ID"""
    corridor = next((c for c in MOCK_CORRIDORS if c["id"] == corridor_id), None)
    if not corridor:
        raise HTTPException(status_code=404, detail="Corridor not found")
    return corridor


@router.post("/", response_model=Corridor, status_code=201)
def create_corridor(corridor: CorridorCreate):
    """Create new corridor"""
    new_corridor = {
        "id": str(len(MOCK_CORRIDORS) + 1),
        **corridor.dict(),
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_CORRIDORS.append(new_corridor)
    return new_corridor


@router.put("/{corridor_id}", response_model=Corridor)
def update_corridor(corridor_id: str, corridor: CorridorCreate):
    """Update existing corridor"""
    corridor_index = next((i for i, c in enumerate(MOCK_CORRIDORS) if c["id"] == corridor_id), None)
    if corridor_index is None:
        raise HTTPException(status_code=404, detail="Corridor not found")
    
    updated_corridor = {
        "id": corridor_id,
        **corridor.dict(),
        "created_at": MOCK_CORRIDORS[corridor_index]["created_at"],
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_CORRIDORS[corridor_index] = updated_corridor
    return updated_corridor


@router.delete("/{corridor_id}")
def delete_corridor(corridor_id: str):
    """Delete corridor"""
    corridor_index = next((i for i, c in enumerate(MOCK_CORRIDORS) if c["id"] == corridor_id), None)
    if corridor_index is None:
        raise HTTPException(status_code=404, detail="Corridor not found")
    
    MOCK_CORRIDORS.pop(corridor_index)
    return {"message": "Corridor deleted", "id": corridor_id}
