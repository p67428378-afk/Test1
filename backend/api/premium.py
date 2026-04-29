
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.schemas.policy import PremiumCalculationRequest, PremiumCalculationResponse
from backend.services.premium_calculator import calculate_premium
from backend.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/premium/calculate", response_model=PremiumCalculationResponse)
def calculate_premium_endpoint(request: PremiumCalculationRequest, db: Session = Depends(get_db)):
    return calculate_premium(request)
