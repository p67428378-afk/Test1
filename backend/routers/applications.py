
from fastapi import APIRouter, Depends, HTTPException, UploadFile, File
from sqlalchemy.orm import Session
from typing import List

from backend.database import get_db
from backend.models import Applicant, Application, Document
from backend.schemas import Applicant as ApplicantSchema, ApplicantCreate, \
    Application as ApplicationSchema, ApplicationCreate, \
    Document as DocumentSchema, DocumentCreate

router = APIRouter()

@router.post("/applicants", response_model=ApplicantSchema)
def create_applicant(applicant: ApplicantCreate, db: Session = Depends(get_db)):
    db_applicant = Applicant(**applicant.model_dump())
    db.add(db_applicant)
    db.commit()
    db.refresh(db_applicant)
    return db_applicant

@router.post("/applications", response_model=ApplicationSchema)
def create_application(application: ApplicationCreate, db: Session = Depends(get_db)):
    # Check if applicant and card exist
    applicant = db.query(Applicant).filter(Applicant.applicant_id == application.applicant_id).first()
    if not applicant:
        raise HTTPException(status_code=404, detail="Applicant not found")
    
    # Assuming CreditCardOffering model is available and imported
    from backend.models import CreditCardOffering
    card_offering = db.query(CreditCardOffering).filter(CreditCardOffering.card_id == application.card_id).first()
    if not card_offering:
        raise HTTPException(status_code=404, detail="Credit card offering not found")

    db_application = Application(**application.model_dump())
    db.add(db_application)
    db.commit()
    db.refresh(db_application)
    return db_application

@router.post("/applications/{application_id}/documents", response_model=DocumentSchema)
def upload_document(
    application_id: int,
    document_type: str,
    file: UploadFile = File(...),
    db: Session = Depends(get_db)
):
    application = db.query(Application).filter(Application.application_id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    
    # In a real scenario, the file would be uploaded to object storage (e.g., S3, GCS)
    # and storage_path would be the URL or reference to that object.
    # For this example, we'll just save the filename and a dummy path.
    storage_path = f"/documents/{application_id}/{file.filename}"
    
    db_document = Document(
        application_id=application_id,
        document_type=document_type,
        file_name=file.filename,
        storage_path=storage_path
    )
    db.add(db_document)
    db.commit()
    db.refresh(db_document)
    
    return db_document
