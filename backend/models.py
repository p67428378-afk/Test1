
from sqlalchemy import Column, Integer, String, Text, DateTime, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from database import Base

class CreditCardOffering(Base):
    __tablename__ = "credit_card_offerings"

    card_id = Column(Integer, primary_key=True, index=True)
    card_name = Column(String, unique=True, index=True, nullable=False)
    features = Column(Text, nullable=True)  # Storing JSON as Text for simplicity
    eligibility_criteria = Column(Text, nullable=True) # Storing JSON as Text for simplicity
    annual_fee = Column(Integer, nullable=False)
    interest_rate = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="credit_card_offering")

class Applicant(Base):
    __tablename__ = "applicants"

    applicant_id = Column(Integer, primary_key=True, index=True)
    full_name = Column(String, nullable=False)
    residential_address = Column(String, nullable=False)
    phone_number = Column(String, nullable=False)
    email_address = Column(String, unique=True, index=True, nullable=False)
    annual_income = Column(Integer, nullable=False)
    credit_score = Column(Integer, nullable=True)
    employer_name = Column(String, nullable=True)
    employer_address = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    employment_start_date = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applications = relationship("Application", back_populates="applicant")

class Application(Base):
    __tablename__ = "applications"

    application_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"), nullable=False)
    card_id = Column(Integer, ForeignKey("credit_card_offerings.card_id"), nullable=False)
    status = Column(String, default="PENDING", nullable=False)
    submission_date = Column(DateTime, default=datetime.utcnow)
    review_flag = Column(Boolean, default=False)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    applicant = relationship("Applicant", back_populates="applications")
    credit_card_offering = relationship("CreditCardOffering", back_populates="applications")
    documents = relationship("Document", back_populates="application")

class Document(Base):
    __tablename__ = "documents"

    document_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.application_id"), nullable=False)
    document_type = Column(String, nullable=False)
    file_name = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    uploaded_at = Column(DateTime, default=datetime.utcnow)

    application = relationship("Application", back_populates="documents")
