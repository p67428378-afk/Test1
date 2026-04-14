from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from .. import schemas
from .. import models
from ..db.database import get_db

router = APIRouter()

@router.post("/", response_model=schemas.Deposit)
def create_deposit_for_account(account_id: int, deposit: schemas.DepositCreate, db: Session = Depends(get_db)):
    db_account = db.query(models.Account).filter(models.Account.id == account_id).first()
    if not db_account:
        raise HTTPException(status_code=404, detail="Account not found")
    db_deposit = models.Deposit(**deposit.dict(), account_id=account_id)
    db.add(db_deposit)
    db.commit()
    db.refresh(db_deposit)
    # For simplicity, we are not updating the account balance here.
    # In a real application, this would be a more complex transaction.
    return db_deposit

@router.get("/{deposit_id}", response_model=schemas.Deposit)
def read_deposit(deposit_id: int, db: Session = Depends(get_db)):
    db_deposit = db.query(models.Deposit).filter(models.Deposit.id == deposit_id).first()
    if db_deposit is None:
        raise HTTPException(status_code=404, detail="Deposit not found")
    return db_deposit
