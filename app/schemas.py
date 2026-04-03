
from pydantic import BaseModel, Field
from datetime import datetime
from typing import List, Optional

class IncomeDetails(BaseModel):
    annual_income: float = Field(..., gt=0, description="Applicant's annual income")
    income_source: str = Field(..., min_length=1, description="Source of income (e.g., Salary, Business)")
    proof_of_income_ref: str = Field(..., min_length=1, description="Reference to income proof document")

class EmploymentDetails(BaseModel):
    employer_name: str = Field(..., min_length=1, description="Name of the employer")
    employment_status: str = Field(..., min_length=1, description="Employment status (e.g., Employed, Self-Employed)")
    years_of_employment: int = Field(..., ge=0, description="Years of employment")

class PersonalDetails(BaseModel):
    name: str = Field(..., min_length=1, description="Applicant's full name")
    dob: str = Field(..., pattern=r"^\d{4}-\d{2}-\d{2}$", description="Date of birth in YYYY-MM-DD format") # Changed regex escaping
    address: str = Field(..., min_length=1, description="Applicant's address")
    pan: str = Field(..., min_length=10, max_length=10, description="Permanent Account Number (PAN)")
    aadhaar: str = Field(..., min_length=12, max_length=12, description="Aadhaar number")

class LoanApplicationRequest(BaseModel):
    applicant_id: str = Field(..., min_length=1, description="Unique identifier for the applicant")
    income_details: IncomeDetails
    credit_score: int = Field(..., ge=300, le=900, description="Applicant's credit score")
    employment_details: EmploymentDetails
    bank_statement_refs: List[str] = Field(..., min_length=1, description="References to bank statement documents")
    personal_details: PersonalDetails

class UnderwritingDecision(BaseModel):
    decision_id: str = Field(..., description="Unique identifier for the underwriting decision")
    applicant_id: str = Field(..., description="Unique identifier for the applicant")
    final_status: str = Field(..., description="Final underwriting status (APPROVED, REJECTED, REVIEW)")
    decision_timestamp: datetime = Field(..., description="Timestamp of the decision")
    risk_score: Optional[float] = Field(None, description="Overall calculated risk score")
    ml_score: Optional[float] = Field(None, description="Score from ML model")
    rbi_check_result: Optional[dict] = Field(None, description="Result of RBI defaulter check")
    triggered_rules: Optional[List[str]] = Field(None, description="List of risk rules that were triggered")
    audit_trail_id: str = Field(..., description="Reference to the audit trail record")

class HealthCheckResponse(BaseModel):
    status: str = Field(..., description="Status of the microservice")
