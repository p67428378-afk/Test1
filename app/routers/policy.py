from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app import crud, schemas, models
from app.database import get_db

router = APIRouter(
    prefix="/policies",
    tags=["policies"],
    responses={404: {"description": "Not found"}},
)

@router.post("/", response_model=schemas.PolicyResponse)
def create_policy(policy_request: schemas.PolicyCreateRequest, db: Session = Depends(get_db)):
    db_policyholder = crud.create_policyholder(db=db, policyholder=policy_request.policyholder)
    db_policy = crud.create_policy(db=db, policy=policy_request.policy, policyholder_id=db_policyholder.policyholder_id)
    return schemas.PolicyResponse(policyholder=db_policyholder, policy=db_policy)

@router.put("/{policy_id}", response_model=schemas.Policy)
def update_policy(policy_id: str, policy_update: schemas.PolicyUpdate, db: Session = Depends(get_db)):
    db_policy = crud.update_policy(db=db, policy_id=policy_id, policy_update=policy_update)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy

@router.post("/{policy_id}/cancel", response_model=schemas.Policy)
def cancel_policy(policy_id: str, db: Session = Depends(get_db)):
    db_policy = crud.cancel_policy(db=db, policy_id=policy_id)
    if db_policy is None:
        raise HTTPException(status_code=404, detail="Policy not found")
    return db_policy
