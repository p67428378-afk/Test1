from sqlalchemy.orm import Session
from app.models import Policyholder, Policy
from app.schemas import PolicyholderCreate, PolicyCreate, PolicyUpdate

def create_policyholder(db: Session, policyholder: PolicyholderCreate):
    db_policyholder = Policyholder(**policyholder.model_dump())
    db.add(db_policyholder)
    db.commit()
    db.refresh(db_policyholder)
    return db_policyholder

def create_policy(db: Session, policy: PolicyCreate, policyholder_id: str):
    db_policy = Policy(**policy.model_dump(), policyholder_id=policyholder_id)
    db.add(db_policy)
    db.commit()
    db.refresh(db_policy)
    return db_policy

def get_policy(db: Session, policy_id: str):
    return db.query(Policy).filter(Policy.policy_id == policy_id).first()

def update_policy(db: Session, policy_id: str, policy_update: PolicyUpdate):
    db_policy = db.query(Policy).filter(Policy.policy_id == policy_id).first()
    if db_policy:
        update_data = policy_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(db_policy, key, value)
        db.add(db_policy)
        db.commit()
        db.refresh(db_policy)
    return db_policy

def cancel_policy(db: Session, policy_id: str):
    db_policy = db.query(Policy).filter(Policy.policy_id == policy_id).first()
    if db_policy:
        db_policy.status = "Cancelled"
        db.add(db_policy)
        db.commit()
        db.refresh(db_policy)
    return db_policy
