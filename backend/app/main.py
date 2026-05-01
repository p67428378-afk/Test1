from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import models, schemas, database

models.Base.metadata.create_all(bind=database.engine)

app = FastAPI()

@app.post("/api/v1/insurance/premium", response_model=schemas.PremiumCalculationResponse)
def calculate_premium(request: schemas.PremiumCalculationRequest, db: Session = Depends(database.get_db)):
    base_premium = 500.0

    # NCB calculation
    if request.ncb_years < 0:
        raise HTTPException(status_code=400, detail="NCB years cannot be negative.")
    
    ncb_discount_percentage = 0
    if 1 <= request.ncb_years <= 5:
        ncb_discount_percentage = 0.10 * request.ncb_years + 0.10
    elif request.ncb_years > 5:
        ncb_discount_percentage = 0.50

    if ncb_discount_percentage > 0.5:
        ncb_discount_percentage = 0.5

    premium_after_ncb = base_premium * (1 - ncb_discount_percentage)

    # Vehicle multiplier
    if not (0.8 <= request.vehicle_risk_factor <= 1.6):
        raise HTTPException(status_code=400, detail="Vehicle risk factor must be between 0.8 and 1.6.")

    calculated_premium = premium_after_ncb * request.vehicle_risk_factor

    # Create policy record
    db_policy = models.Policy(
        policy_holder_name=request.policy_holder_name,
        vehicle_type=request.vehicle_type,
        ncb_years=request.ncb_years,
        vehicle_risk_factor=request.vehicle_risk_factor,
        base_premium=base_premium,
        ncb_discount_percentage=ncb_discount_percentage,
        vehicle_multiplier_applied=request.vehicle_risk_factor,
        calculated_premium=calculated_premium
    )
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)

    return schemas.PremiumCalculationResponse(
        calculated_premium=calculated_premium,
        policy_id=db_policy.policy_id
    )
