
from sqlalchemy import Column, Integer, String, Text, Boolean, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Card(Base):
    __tablename__ = "cards"
    card_id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True, nullable=False)
    description = Column(Text, nullable=False)
    features = Column(Text, nullable=False)
    apr = Column(String, nullable=False)
    annual_fee = Column(String, nullable=False)
    eligibility_criteria = Column(Text, nullable=False)
    terms_conditions_url = Column(String, nullable=False)

class Applicant(Base):
    __tablename__ = "applicants"
    applicant_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String, nullable=False)
    date_of_birth = Column(String, nullable=False) # Encrypted in real app, but string for now
    ssn = Column(String, nullable=False) # Encrypted in real app, but string for now
    address = Column(Text, nullable=False)

class Application(Base):
    __tablename__ = "applications"
    application_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"), nullable=False)
    card_id = Column(Integer, ForeignKey("cards.card_id"), nullable=False)
    submission_date = Column(Date, nullable=False)
    status = Column(String, default="Pending", nullable=False)
    employment_status = Column(String, nullable=False)
    annual_income = Column(String, nullable=False) # Encrypted in real app, but string for now
    existing_debts = Column(String, nullable=False) # Encrypted in real app, but string for now
    consent_credit_check = Column(Boolean, nullable=False)

    applicant = relationship("Applicant", backref="applications")
    card = relationship("Card", backref="applications")

class Document(Base):
    __tablename__ = "documents"
    document_id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey("applications.application_id"), nullable=False)
    document_type = Column(String, nullable=False)
    storage_path = Column(String, nullable=False)
    upload_date = Column(Date, nullable=False)
    encrypted = Column(Boolean, nullable=False)

    application = relationship("Application", backref="documents")
