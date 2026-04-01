
from pydantic import BaseModel, Field, EmailStr
from typing import Optional
from datetime import datetime

class BaseSchema(BaseModel):
    class Config:
        from_attributes = True

class CreditCardOfferingBase(BaseSchema):
    card_name: str
    features: str
    eligibility_criteria: str
    annual_fee: float
    interest_rate: float

class CreditCardOfferingCreate(CreditCardOfferingBase):
    pass

class CreditCardOffering(CreditCardOfferingBase):
    card_id: int
    created_at: datetime
    updated_at: datetime

class ApplicantBase(BaseSchema):
    full_name: str
    residential_address: str
    phone_number: str
    email_address: EmailStr # Changed to EmailStr for email validation
    annual_income: float
    credit_score: int
    employer_name: str
    employer_address: str
    job_title: str
    employment_start_date: str

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    applicant_id: int
    created_at: datetime
    updated_at: datetime

class ApplicationBase(BaseSchema):
    applicant_id: int
    card_id: int
    status: str = "PENDING"
    review_flag: bool = True

class ApplicationCreate(ApplicationBase):
    pass

class Application(ApplicationBase):
    application_id: int
    submission_date: datetime
    created_at: datetime
    updated_at: datetime

class DocumentBase(BaseSchema):
    application_id: int
    document_type: str
    file_name: str
    storage_path: str

class DocumentCreate(DocumentBase):
    pass

class Document(DocumentBase):
    document_id: int
    uploaded_at: datetime
