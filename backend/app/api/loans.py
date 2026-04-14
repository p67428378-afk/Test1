from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from .. import models
from ..db.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Loan)
def create_loan_for_user(user_id: int, loan: schemas.LoanCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=404, detail="User not found")
    db_loan = models.Loan(**loan.dict(), owner_id=user_id)
    db.add(db_loan)
    db.commit()
    db.refresh(db_loan)
    return db_loan

@router.get("/{loan_id}", response_model=schemas.Loan)
def read_loan(loan_id: int, db: Session = Depends(get_db)):
    db_loan = db.query(models.Loan).filter(models.Loan.id == loan_id).first()
    if db_loan is None:
        raise HTTPException(status_code=404, detail="Loan not found")
    return db_loan
