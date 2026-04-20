from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from .. import models, schemas, database
from .auth import get_current_user
import uuid

router = APIRouter(
    prefix="/flat-transfer",
    tags=["flat-transfer"],
)

@router.post("/initiate", response_model=schemas.FlatTransferRequest)
def initiate_flat_transfer_request(
    request: schemas.FlatTransferRequestCreate,
    db: Session = Depends(database.get_db),
    current_user: models.User = Depends(get_current_user)
):
    if current_user.role != "admin":
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Only admins can initiate a flat transfer request."
        )

    buyer = db.query(models.Member).filter(models.Member.email == request.buyer_email).first()
    if not buyer:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Buyer with email {request.buyer_email} not found."
        )

    seller = db.query(models.Member).filter(models.Member.email == request.seller_email).first()
    if not seller:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Seller with email {request.seller_email} not found."
        )

    flat = db.query(models.Property).filter(models.Property.id == request.flat_id).first()
    if not flat:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Flat with id {request.flat_id} not found."
        )

    application_number = f"FP-{uuid.uuid4().hex[:6].upper()}-{flat.id}"

    db_request = models.FlatTransferRequest(
        buyer_id=buyer.id,
        seller_id=seller.id,
        flat_id=flat.id,
        transaction_type=request.transaction_type,
        initiated_by=current_user.id,
        application_number=application_number
    )
    db.add(db_request)
    db.commit()
    db.refresh(db_request)
    return db_request
