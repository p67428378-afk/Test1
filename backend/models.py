
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Boolean, Text
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()

class Applicant(Base):
    __tablename__ = "applicants"

    applicant_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, index=True)
    residential_address = Column(String)
    phone_number = Column(String)
    email_address = Column(String, unique=True, index=True)
    annual_income = Column(Float)
    credit_score = Column(Integer)
    employer_name = Column(String)
    employer_address = Column(String)
    job_title = Column(String)
    employment_start_date = Column(String) # Storing as string for simplicity, can be Date type
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="applicant")

class CreditCardOffering(Base):
    __tablename__ = "credit_card_offerings"

    card_id = Column(Integer, primary_key=True, index=True)
    card_name = Column(String, unique=True, index=True)
    features = Column(Text) # Storing as Text, can be JSONB in PostgreSQL
    eligibility_criteria = Column(Text) # Storing as Text, can be JSONB in PostgreSQL
    annual_fee = Column(Float)
    interest_rate = Column(Float)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="credit_card_offering")

class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"))
    card_id = Column(Integer, ForeignKey("credit_card_offerings.card_id"))
    status = Column(String, default="PENDING") # e.g., 'PENDING', 'UNDER_REVIEW', 'APPROVED', 'REJECTED'
    submission_date = Column(DateTime, default=datetime.utcnow)
    review_flag = Column(Boolean, default=True) # Flag for manual review
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applicant = relationship("Applicant", back_populates="applications")
    credit_card_offering = relationship("CreditCardOffering", back_populates="applications")
    documents = relationship("Document", back_populates="application")

class Document(Base):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.application_id"))
    document_type = Column(String) # e.g., 'ACCOUNT_STATEMENT', 'ID_PROOF'
    file_name = Column(String)
    storage_path = Column(String) # URL/Reference to object storage
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("Application", back_populates="documents")
