
from typing import List

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(
    prefix="/cards",
    tags=["cards"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Card)
def create_card(card: schemas.CardCreate, db: Session = Depends(get_db)):
    db_card = models.Card(**card.model_dump())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

@router.get("/", response_model=List[schemas.Card])
def read_cards(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = db.query(models.Card).offset(skip).limit(limit).all()
    return cards

@router.get("/{card_id}", response_model=schemas.Card)
def read_card(card_id: int, db: Session = Depends(get_db)):
    card = db.query(models.Card).filter(models.Card.card_id == card_id).first()
    if card is None:
        raise HTTPException(status_code=404, detail="Card not found")
    return card
