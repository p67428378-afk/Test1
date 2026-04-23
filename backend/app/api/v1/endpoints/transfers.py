
from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from ....schemas.transfer import CancellationRequest, CancellationResponse
from ....services.cancellation_service import CancellationService
from ....db.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/transfers/cancel", response_model=CancellationResponse)
def cancel_transfer(request: CancellationRequest, db: Session = Depends(get_db)):
    service = CancellationService(db)
    try:
        result = service.cancel_transfer(request.transferReferenceId, request.accountNumber)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
