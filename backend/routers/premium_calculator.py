from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from .. import schemas
from ..services import calculate_premium
from ..database import get_db

router = APIRouter()


@router.post("/api/v1/premium-calculator", response_model=schemas.PremiumResponse)
def premium_calculator_endpoint(request: schemas.PremiumRequest, db: Session = Depends(get_db)):
    return calculate_premium(request, db)
