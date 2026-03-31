
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend.database import get_db
from backend.models import CreditCardOffering
from backend.schemas import CreditCardOffering as CreditCardOfferingSchema

router = APIRouter()

@router.get("/credit-cards", response_model=List[CreditCardOfferingSchema])
def get_credit_card_offerings(db: Session = Depends(get_db)):
    offerings = db.query(CreditCardOffering).all()
    return offerings

@router.get("/credit-cards/{card_id}", response_model=CreditCardOfferingSchema)
def get_credit_card_offering(card_id: int, db: Session = Depends(get_db)):
    offering = db.query(CreditCardOffering).filter(CreditCardOffering.card_id == card_id).first()
    if offering is None:
        raise HTTPException(status_code=404, detail="Credit card offering not found")
    return offering
