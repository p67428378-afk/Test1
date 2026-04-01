
from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional, List

class CreditCardOfferingBase(BaseModel):
    card_name: str
    features: Optional[str] = None  # Will store JSON string
    eligibility_criteria: Optional[str] = None  # Will store JSON string
    annual_fee: int
    interest_rate: str

class CreditCardOfferingCreate(CreditCardOfferingBase):
    pass

class CreditCardOffering(CreditCardOfferingBase):
    card_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class ApplicantBase(BaseModel):
    full_name: str
    residential_address: str
    phone_number: str
    email_address: EmailStr
    annual_income: int
    credit_score: Optional[int] = None
    employer_name: Optional[str] = None
    employer_address: Optional[str] = None
    job_title: Optional[str] = None
    employment_start_date: Optional[datetime] = None

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    applicant_id: int
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True

class DocumentBase(BaseModel):
    document_type: str
    file_name: str
    storage_path: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    document_id: int
    application_id: int
    uploaded_at: datetime

    class Config:
        from_attributes = True

class ApplicationBase(BaseModel):
    applicant_id: int
    card_id: int
    status: str = "PENDING"
    review_flag: bool = False

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    application_id: int
    submission_date: datetime
    created_at: datetime
    updated_at: datetime
    applicant: Optional[Applicant] = None
    credit_card_offering: Optional[CreditCardOffering] = None
    documents: List[Document] = []

    class Config:
        from_attributes = True
