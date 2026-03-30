from sqlalchemy.orm import Session
from backend.models import Claim
from backend.schemas import ClaimCreate, ClaimUpdate

def create_claim(db: Session, claim: ClaimCreate):
    db_claim = Claim(**claim.model_dump())
    db.add(db_claim)
    db.commit()
    db.refresh(db_claim)
    return db_claim

def get_claim(db: Session, claim_id: str):
    return db.query(Claim).filter(Claim.claim_id == claim_id).first()

def approve_claim(db: Session, claim_id: str, approved_by_agent_id: str):
    db_claim = db.query(Claim).filter(Claim.claim_id == claim_id).first()
    if db_claim:
        db_claim.status = "SIMPLE_APPROVED"
        db_claim.approved_by_agent_id = approved_by_agent_id
        db.commit()
        db.refresh(db_claim)
    return db_claim
