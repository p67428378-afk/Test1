
from datetime import date
from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session

import models, schemas
from database import get_db

router = APIRouter(
    prefix="/applications",
    tags=["applications"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Application, status_code=status.HTTP_200_OK)
def create_application(application: schemas.ApplicationCreate, db: Session = Depends(get_db)):
    # Check if applicant and card exist
    db_applicant = db.query(models.Applicant).filter(models.Applicant.applicant_id == application.applicant_id).first()
    if not db_applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")

    db_card = db.query(models.Card).filter(models.Card.card_id == application.card_id).first()
    if not db_card:
        raise HTTPException(status_code=404, detail="Card not found")

    db_application = models.Application(
        **application.model_dump(),
        submission_date=date.today(),
        status="Pending"
    )
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.post("/applicant/", response_model=schemas.Applicant, status_code=status.HTTP_200_OK)
def create_applicant(applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = models.Applicant(**applicant.model_dump())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant
