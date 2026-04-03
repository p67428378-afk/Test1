
from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from datetime import date

import models, schemas
from database import SessionLocal, engine, get_db

models.Base.metadata.create_all(bind=engine)

app = FastAPI()

# Dependency to get DB session

@app.on_event("startup")
async def startup_event():
    db = SessionLocal()
    try:
        # Add some dummy credit card offers if none exist
        if db.query(models.CreditCardOffer).count() == 0:
            offers = [
                models.CreditCardOffer(
                    name="Platinum Rewards Card",
                    description="Earn points on every purchase.",
                    apr=19.99,
                    annual_fee=99.00,
                    rewards_program="2x points on travel and dining",
                    eligibility_criteria="Excellent credit"
                ),
                models.CreditCardOffer(
                    name="Travel Miles Card",
                    description="No foreign transaction fees, earn miles.",
                    apr=17.50,
                    annual_fee=75.00,
                    rewards_program="1.5x miles on all purchases",
                    eligibility_criteria="Good to excellent credit"
                ),
                models.CreditCardOffer(
                    name="Student Starter Card",
                    description="Build your credit history.",
                    apr=22.99,
                    annual_fee=0.00,
                    rewards_program="None",
                    eligibility_criteria="No credit history required"
                )
            ]
            db.add_all(offers)
            db.commit()
    finally:
        db.close()

@app.get("/credit-card-offers/", response_model=List[schemas.CreditCardOffer])
def read_credit_card_offers(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    offers = db.query(models.CreditCardOffer).offset(skip).limit(limit).all()
    return offers

@app.post("/applicants/", response_model=schemas.Applicant, status_code=status.HTTP_200_OK)
def create_applicant(applicant: schemas.ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = models.Applicant(**applicant.model_dump())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

@app.post("/applicants/{applicant_id}/financial-info", response_model=schemas.Applicant, status_code=status.HTTP_200_OK)
def update_applicant_financial_info(
    applicant_id: str,
    financial_info: schemas.ApplicantUpdateFinancial,
    db: Session = Depends(get_db)
):
    db_applicant = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")

    db_applicant.annual_income = financial_info.annual_income
    db_applicant.credit_score = financial_info.credit_score
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

@app.post("/applicants/{applicant_id}/employment-info", response_model=schemas.Applicant, status_code=status.HTTP_200_OK)
def update_applicant_employment_info(
    applicant_id: str,
    employment_info: schemas.ApplicantUpdateEmployment,
    db: Session = Depends(get_db)
):
    db_applicant = db.query(models.Applicant).filter(models.Applicant.id == applicant_id).first()
    if db_applicant is None:
        raise HTTPException(status_code=404, detail="Applicant not found")

    db_applicant.employer_name = employment_info.employer_name
    db_applicant.employer_address = employment_info.employer_address
    db_applicant.job_title = employment_info.job_title
    db_applicant.employment_start_date = employment_info.employment_start_date
    db.commit()
    db.refresh(db_applicant)
    return db_applicant
