from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from backend import schemas
from backend.services import claim_service
from backend.database import get_db

router = APIRouter(
    prefix="/claims",
    tags=["claims"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.Claim)
def create_claim(claim: schemas.ClaimCreate, db: Session = Depends(get_db)):
    return claim_service.create_claim(db=db, claim=claim)

@router.post("/{claim_id}/approve", response_model=schemas.Claim)
def approve_claim(claim_id: str, approved_by: schemas.ClaimApprove, db: Session = Depends(get_db)):
    db_claim = claim_service.approve_claim(db=db, claim_id=claim_id, approved_by_agent_id=approved_by.approved_by_agent_id)
    if db_claim is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim
