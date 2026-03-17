from pydantic import BaseModel, EmailStr, Field
from datetime import date
from typing import Optional

class ApplicantBase(BaseModel):
    first_name: str = Field(..., min_length=1, max_length=100)
    last_name: str = Field(..., min_length=1, max_length=100)
    date_of_birth: date
    ssn: str = Field(..., min_length=9, max_length=11, pattern=r"^\d{3}-\d{2}-\d{4}$|^\d{9}$") # Format XXX-XX-XXXX or XXXXXXXXX
    email: EmailStr
    phone_number: str = Field(..., min_length=10, max_length=20)
    address: str = Field(..., min_length=5, max_length=200)

class ApplicantCreate(ApplicantBase):
    pass

class Applicant(ApplicantBase):
    applicant_id: int

    class Config:
        from_attributes = True

class EmploymentBase(BaseModel):
    company_name: str = Field(..., min_length=1, max_length=100)
    company_address: str = Field(..., min_length=5, max_length=200)
    job_title: str = Field(..., min_length=1, max_length=100)
    income: float = Field(..., gt=0)

class EmploymentCreate(EmploymentBase):
    pass

class Employment(EmploymentBase):
    employment_id: int
    applicant_id: int

    class Config:
        from_attributes = True

class BankAccountBase(BaseModel):
    account_number: str = Field(..., min_length=5, max_length=20)
    aba_routing_number: str = Field(..., min_length=9, max_length=9, pattern=r"^\d{9}$")

class BankAccountCreate(BankAccountBase):
    pass

class BankAccount(BankAccountBase):
    bank_account_id: int
    applicant_id: int

    class Config:
        from_attributes = True

class LoanApplicationBase(BaseModel):
    loan_purpose: str = Field(..., min_length=3, max_length=200)
    loan_amount: float = Field(..., gt=0)
    loan_period_months: int = Field(..., gt=0)

class LoanApplicationCreate(LoanApplicationBase):
    pass

class LoanApplication(LoanApplicationBase):
    application_id: int
    applicant_id: int
    submission_date: date
    status: str

    class Config:
        from_attributes = True

class LegalDeclarationBase(BaseModel):
    citizenship_status: str = Field(..., min_length=1, max_length=50)
    has_pending_cases: bool

class LegalDeclarationCreate(LegalDeclarationBase):
    pass

class LegalDeclaration(LegalDeclarationBase):
    legal_id: int
    applicant_id: int
    declaration_date: date

    class Config:
        from_attributes = True

class LoanApplicationForm(BaseModel):
    applicant: ApplicantCreate
    employment: EmploymentCreate
    bank_account: BankAccountCreate
    loan_details: LoanApplicationCreate
    legal_declaration: LegalDeclarationCreate

class LoanApplicationResponse(BaseModel):
    applicant: Applicant
    employment: Employment
    bank_account: BankAccount
    loan_application: LoanApplication
    legal_declaration: LegalDeclaration

    class Config:
        from_attributes = True
