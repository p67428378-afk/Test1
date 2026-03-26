from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from schemas import LoanApplicationCreate, LoanApplicationResponse
from services import create_loan_application
from database import get_db

router = APIRouter()

@router.post("/applications", status_code=status.HTTP_200_OK)
def submit_loan_application(
    application: LoanApplicationCreate,
    db: Session = Depends(get_db)
):
    print("--- Inside submit_loan_application endpoint ---")
    try:
        db_loan_application = create_loan_application(db=db, application=application)
        return {"message": "Loan application submitted successfully", "application_id": db_loan_application.application_id}
    except ValueError as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=str(e))
