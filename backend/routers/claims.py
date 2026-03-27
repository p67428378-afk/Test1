from typing import List
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.core.database import get_db
from backend.schemas.claim import ClaimCreate, ClaimResponse, ClaimSummaryResponse
from backend.services import claim_service

router = APIRouter()

@router.post("/", response_model=ClaimResponse)
def create_new_claim(claim: ClaimCreate, db: Session = Depends(get_db)):
    db_claim_response = claim_service.create_claim(db=db, claim=claim) # Renamed variable
    return db_claim_response

@router.post("/{claim_id}/approve", response_model=ClaimResponse)
def approve_claim_route(claim_id: str, db: Session = Depends(get_db)):
    db_claim_response = claim_service.approve_claim(db=db, claim_id=claim_id) # Renamed variable
    if db_claim_response is None:
        raise HTTPException(status_code=404, detail="Claim not found")
    return db_claim_response

@router.get("/{claim_id}/summary", response_model=ClaimSummaryResponse)
def get_claim_summary_route(claim_id: str, db: Session = Depends(get_db)):
    summary = claim_service.get_claim_summary(db=db, claim_id=claim_id)
    if summary is None:
        raise HTTPException(status_code=404, detail="Claim not found or summary not available")
    return summary
