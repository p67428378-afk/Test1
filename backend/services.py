from sqlalchemy.orm import Session
from . import models, schemas

BASE_PREMIUM = 500.0

NCB_DISCOUNTS = {
    "0_years": 0.20,
    "1_year": 0.20,
    "2_years": 0.25,
    "3_years": 0.35,
    "4_years": 0.45,
    "5_years_or_more": 0.50,
}

VEHICLE_MULTIPLIERS = {
    "sedan": 1.0,
    "suv": 1.2,
    "hatchback": 0.9,
    "truck": 1.5,
}

def get_db():
    db = None
    try:
        db = models.SessionLocal()
        yield db
    finally:
        if db:
            db.close()

def calculate_premium(request: schemas.PremiumRequest, db: Session):
    ncb_discount = NCB_DISCOUNTS.get(request.ncb_level, 0.20)
    if ncb_discount < 0.20:
        ncb_discount = 0.20
    if ncb_discount > 0.50:
        ncb_discount = 0.50

    premium_after_ncb = BASE_PREMIUM * (1 - ncb_discount)

    vehicle_multiplier = VEHICLE_MULTIPLIERS.get(request.vehicle_type.lower(), 1.0)
    if vehicle_multiplier < 0.8:
        vehicle_multiplier = 0.8
    if vehicle_multiplier > 1.6:
        vehicle_multiplier = 1.6

    final_premium = premium_after_ncb * vehicle_multiplier

    return schemas.PremiumResponse(calculated_premium=final_premium)
