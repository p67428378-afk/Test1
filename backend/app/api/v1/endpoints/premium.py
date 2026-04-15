from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.schemas.policy import PremiumCalculationRequest, PremiumCalculationResponse
from app.services.premium_calculator import calculate_premium
from app.db.database import get_db

router = APIRouter()

@router.post("/premium/calculate", response_model=PremiumCalculationResponse)
def calculate_premium_endpoint(request: PremiumCalculationRequest, db: Session = Depends(get_db)):
    """
    Calculates the insurance premium based on the provided data.
    """
    premium = calculate_premium(
        base_rate=request.base_rate,
        ncb_years=request.ncb_years,
        vehicle_multiplier=request.vehicle_multiplier
    )
    return {"calculated_premium": premium}
