# import json # No longer needed here
from typing import List, Optional
from datetime import datetime # Import datetime
from sqlalchemy.orm import Session
from backend.models.claim import Claim
from backend.schemas.claim import ClaimCreate, ClaimStatus, ClaimResponse, ClaimSummaryResponse

def create_claim(db: Session, claim: ClaimCreate) -> ClaimResponse: # Changed return type
    current_time = datetime.now() # Get current time
    db_claim = Claim(
        claim_type=claim.claim_type.value,
        claimant_name=claim.claimant_name,
        policy_number=claim.policy_number,
        claim_amount=claim.claim_amount,
        incident_description=claim.incident_description,
        document_references=claim.document_references, # Use directly, custom type handles serialization
        status=ClaimStatus.PENDING.value,
        created_at=current_time, # Explicitly set
        updated_at=current_time # Explicitly set
    )
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return ClaimResponse.model_validate(db_claim) # Manually validate

def get_claim(db: Session, claim_id: str) -> Optional[ClaimResponse]: # Changed return type
    db_claim = db.query(Claim).filter(Claim.claim_id == claim_id).first()
    if db_claim:
        return ClaimResponse.model_validate(db_claim) # Manually validate
    return None

def approve_claim(db: Session, claim_id: str) -> Optional[ClaimResponse]: # Changed return type
    db_claim = db.query(Claim).filter(Claim.claim_id == claim_id).first()
    if db_claim:
        # Simple approval logic: if amount is under $1000, approve, else flag for complex review
        if db_claim.claim_amount < 1000:
            db_claim.status = ClaimStatus.SIMPLE_APPROVED.value
        else:
            db_claim.status = ClaimStatus.COMPLEX_REVIEW.value
        db.commit()
        db.refresh(db_claim)
        return ClaimResponse.model_validate(db_claim) # Manually validate
    return None

def get_claim_summary(db: Session, claim_id: str) -> Optional[ClaimSummaryResponse]:
    db_claim = db.query(Claim).filter(Claim.claim_id == claim_id).first()
    if db_claim:
        return ClaimSummaryResponse.model_validate(db_claim) # Manually validate
    return None
