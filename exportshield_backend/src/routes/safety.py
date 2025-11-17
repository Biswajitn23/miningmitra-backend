from fastapi import APIRouter, Query

from services.safety_service import calculate_safety_score


router = APIRouter(prefix="/api", tags=["Safety"])


@router.get("/safety")
def get_safety_score(
    temperature: float = Query(..., description="Current tunnel temperature in °C"),
    vibration: float = Query(..., description="Detected vibration level in mm/s"),
) -> dict:
    """
    Get the safety score for the provided temperature and vibration readings.
    """
    safety_score = calculate_safety_score(temperature, vibration)
    return {"safety_score": safety_score}
