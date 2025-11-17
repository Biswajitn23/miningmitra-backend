from fastapi import APIRouter, HTTPException
from typing import List, Optional, Dict
from datetime import datetime
from pydantic import BaseModel

router = APIRouter(prefix="/api/incidents", tags=["Incidents"])


# Pydantic models
class IncidentCreate(BaseModel):
    type: str
    severity: str
    zone: str
    latitude: float
    longitude: float
    title: str
    description: str
    status: Optional[str] = "active"
    affected_workers: Optional[int] = 0


class Incident(BaseModel):
    id: str
    type: str
    severity: str
    zone: str
    latitude: float
    longitude: float
    title: str
    description: str
    status: str
    affected_workers: int
    created_at: str
    updated_at: str


# Mock data
MOCK_INCIDENTS = [
    {
        "id": "1",
        "type": "Gas Leak",
        "severity": "high",
        "zone": "Zone B",
        "latitude": 23.5825,
        "longitude": 87.2720,
        "title": "Gas Leak Detected",
        "description": "Elevated methane levels detected in Zone B tunnel section",
        "status": "active",
        "affected_workers": 5,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "2",
        "type": "Equipment Failure",
        "severity": "medium",
        "zone": "Zone A",
        "latitude": 23.5820,
        "longitude": 87.2718,
        "title": "Drill Malfunction",
        "description": "Primary drill experienced mechanical failure",
        "status": "resolved",
        "affected_workers": 2,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "3",
        "type": "Structural Issue",
        "severity": "critical",
        "zone": "Zone C",
        "latitude": 23.5830,
        "longitude": 87.2730,
        "title": "Tunnel Collapse Risk",
        "description": "Cracks detected in support beams - immediate evacuation required",
        "status": "active",
        "affected_workers": 12,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
    {
        "id": "4",
        "type": "Health Emergency",
        "severity": "high",
        "zone": "Zone A",
        "latitude": 23.5815,
        "longitude": 87.2715,
        "title": "Worker Heat Exhaustion",
        "description": "Multiple workers showing signs of heat stress",
        "status": "active",
        "affected_workers": 3,
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    },
]


@router.get("/", response_model=List[Incident])
def get_all_incidents():
    """Get all incidents"""
    return MOCK_INCIDENTS


@router.get("/active", response_model=List[Incident])
def get_active_incidents():
    """Get all active incidents"""
    return [i for i in MOCK_INCIDENTS if i["status"] == "active"]


@router.get("/critical", response_model=List[Incident])
def get_critical_incidents():
    """Get critical severity incidents"""
    return [i for i in MOCK_INCIDENTS if i["severity"] == "critical" or i["severity"] == "high"]


@router.get("/heatmap")
def get_incident_heatmap() -> Dict[str, int]:
    """Get incident count by zone for heatmap visualization"""
    heatmap = {}
    for incident in MOCK_INCIDENTS:
        zone = incident["zone"]
        heatmap[zone] = heatmap.get(zone, 0) + 1
    return heatmap


@router.get("/{incident_id}", response_model=Incident)
def get_incident(incident_id: str):
    """Get specific incident by ID"""
    incident = next((i for i in MOCK_INCIDENTS if i["id"] == incident_id), None)
    if not incident:
        raise HTTPException(status_code=404, detail="Incident not found")
    return incident


@router.post("/", response_model=Incident, status_code=201)
def create_incident(incident: IncidentCreate):
    """Create new incident"""
    new_incident = {
        "id": str(len(MOCK_INCIDENTS) + 1),
        **incident.dict(),
        "created_at": datetime.utcnow().isoformat() + "Z",
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_INCIDENTS.append(new_incident)
    return new_incident


@router.put("/{incident_id}", response_model=Incident)
def update_incident(incident_id: str, incident: IncidentCreate):
    """Update existing incident"""
    incident_index = next((i for i, inc in enumerate(MOCK_INCIDENTS) if inc["id"] == incident_id), None)
    if incident_index is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    updated_incident = {
        "id": incident_id,
        **incident.dict(),
        "created_at": MOCK_INCIDENTS[incident_index]["created_at"],
        "updated_at": datetime.utcnow().isoformat() + "Z",
    }
    MOCK_INCIDENTS[incident_index] = updated_incident
    return updated_incident


@router.delete("/{incident_id}")
def delete_incident(incident_id: str):
    """Delete incident"""
    incident_index = next((i for i, inc in enumerate(MOCK_INCIDENTS) if inc["id"] == incident_id), None)
    if incident_index is None:
        raise HTTPException(status_code=404, detail="Incident not found")
    
    MOCK_INCIDENTS.pop(incident_index)
    return {"message": "Incident deleted", "id": incident_id}
