from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend import schemas, database

router = APIRouter()

@router.post("/insurance/premium", response_model=schemas.PremiumCalculationResponse)
def calculate_premium(request: schemas.PremiumCalculationRequest, db: Session = Depends(database.get_db)):
    if request.ncb_years < 0:
        raise HTTPException(status_code=422, detail="NCB years must be a non-negative integer.")

    base_premium = 500.0

    # Tiered No Claims Bonus (NCB) Application
    if request.ncb_years >= 4:
        ncb_discount = 0.5
    elif request.ncb_years == 3:
        ncb_discount = 0.4
    elif request.ncb_years == 2:
        ncb_discount = 0.3
    elif request.ncb_years == 1:
        ncb_discount = 0.2
    else:
        ncb_discount = 0.0
    
    premium_after_ncb = base_premium * (1 - ncb_discount)

    # Vehicle Multiplier Application
    if request.vehicle_make == "Ferrari":
        vehicle_multiplier = 1.6
    elif request.vehicle_make == "Toyota":
        vehicle_multiplier = 0.8
    else:
        vehicle_multiplier = 1.0

    final_premium = premium_after_ncb * vehicle_multiplier

    return schemas.PremiumCalculationResponse(premium=final_premium)
