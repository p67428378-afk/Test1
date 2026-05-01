
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import schemas
from backend.database import get_db
from backend.app.services.premium_calculator import PremiumCalculatorService

router = APIRouter()

@router.post("/insurance/premium", response_model=schemas.PremiumCalculationResponse)
def calculate_premium(
    request: schemas.PremiumCalculationRequest, 
    db: Session = Depends(get_db),
    premium_calculator: PremiumCalculatorService = Depends(PremiumCalculatorService)
):
    try:
        final_premium = premium_calculator.calculate(request)
        return schemas.PremiumCalculationResponse(premium=final_premium)
    except ValueError as e:
        raise HTTPException(status_code=422, detail=str(e))
