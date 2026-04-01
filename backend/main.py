
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from database import SessionLocal, engine, get_db
import models, schemas

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Credit Card Offerings Endpoints
@app.post("/credit_card_offerings/", response_model=schemas.CreditCardOffering)
def create_credit_card_offering(
    card: schemas.CreditCardOfferingCreate, db: Session = Depends(get_db)
):
    db_card = db.query(models.CreditCardOffering).filter(
        models.CreditCardOffering.card_name == card.card_name
    ).first()
    if db_card:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="CreditCardOffering with this name already exists"
        )
    db_card = models.CreditCardOffering(**card.model_dump())
    db.add(db_card)
    db.commit()
    db.refresh(db_card)
    return db_card

@app.get("/credit_card_offerings/", response_model=List[schemas.CreditCardOffering])
def get_credit_card_offerings(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    cards = db.query(models.CreditCardOffering).offset(skip).limit(limit).all()
    return cards

@app.get("/credit_card_offerings/{card_id}", response_model=schemas.CreditCardOffering)
def get_credit_card_offering(card_id: int, db: Session = Depends(get_db)):
    card = db.query(models.CreditCardOffering).filter(
        models.CreditCardOffering.card_id == card_id
    ).first()
    if card is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="CreditCardOffering not found"
        )
    return card

# Placeholder for other services (Applicant, Application, Document)
# These will be implemented as separate routers later
