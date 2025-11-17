from fastapi import APIRouter, Query

from src.services.pollution_service import calculate_pollution_index


router = APIRouter(prefix="/api", tags=["Pollution"])


@router.get("/pollution")
def get_pollution_index(
    depth: float = Query(..., description="Drilling depth in meters"),
    explosives: float = Query(..., description="Explosives quantity in kilograms"),
) -> dict:
    """
    Get the pollution index for the provided depth and explosives usage.
    """
    pollution_index = calculate_pollution_index(depth, explosives)
    return {"pollution_index": pollution_index}
