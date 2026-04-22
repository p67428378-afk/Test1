from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.schemas.policy import PremiumCalculationRequest, PremiumCalculationResponse, PolicyDetails
from app.core.database import get_db

router = APIRouter()

@router.post("/premium", response_model=PremiumCalculationResponse)
def calculate_premium(request: PremiumCalculationRequest, db: Session = Depends(get_db)):
    base_premium = 500.0
    calculated_premium = base_premium * (1 - request.no_claims_bonus_percentage) * request.vehicle_multiplier

    policy_details = PolicyDetails(
        vehicle_type=request.vehicle_type,
        no_claims_bonus_percentage=request.no_claims_bonus_percentage,
        vehicle_multiplier=request.vehicle_multiplier,
        base_premium=base_premium
    )

    return PremiumCalculationResponse(
        calculated_premium=calculated_premium,
        policy_details=policy_details
    )
