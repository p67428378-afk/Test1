from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey, Text
from sqlalchemy.orm import relationship
from database import Base
import uuid

class Applicant(Base):
    __tablename__ = "applicants"

    applicant_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    date_of_birth = Column(Date)
    ssn = Column(String) # Encrypted in real-world scenario
    address = Column(String)
    phone_number = Column(String)
    email_address = Column(String, unique=True, index=True)

    employment = relationship("Employment", back_populates="applicant", uselist=False)
    financial = relationship("Financial", back_populates="applicant", uselist=False)
    loan_applications = relationship("LoanApplication", back_populates="applicant")

class Employment(Base):
    __tablename__ = "employment_info"

    employment_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    applicant_id = Column(String, ForeignKey("applicants.applicant_id"))
    employer_name = Column(String)
    job_title = Column(String)
    annual_income = Column(Float)
    employment_start_date = Column(Date)

    applicant = relationship("Applicant", back_populates="employment")

class Financial(Base):
    __tablename__ = "financial_info"

    financial_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    applicant_id = Column(String, ForeignKey("applicants.applicant_id"))
    bank_account_number = Column(String) # Encrypted in real-world scenario
    routing_number = Column(String) # Encrypted in real-world scenario
    credit_score = Column(Integer)
    existing_debts = Column(Text) # Stored as JSON/Text as per HLD
    assets = Column(Text) # Stored as JSON/Text as per HLD

    applicant = relationship("Applicant", back_populates="financial")

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    application_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    applicant_id = Column(String, ForeignKey("applicants.applicant_id"))
    loan_amount = Column(Float)
    loan_purpose = Column(String)
    repayment_period_months = Column(Integer)
    submission_date = Column(Date)
    status = Column(String, default="Submitted")
    kyc_status = Column(String, default="Pending")
    credit_check_status = Column(String, default="Pending")

    applicant = relationship("Applicant", back_populates="loan_applications")
