
import uuid
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class CreditCardOffer(Base):
    __tablename__ = "credit_card_offers"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    description = Column(String)
    apr = Column(Float)
    annual_fee = Column(Float)
    rewards_program = Column(String, nullable=True)
    eligibility_criteria = Column(String, nullable=True)

    applications = relationship("Application", back_populates="credit_card_offer")

class Applicant(Base):
    __tablename__ = "applicants"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    first_name = Column(String)
    last_name = Column(String)
    address = Column(String)
    phone_number = Column(String)
    email = Column(String, unique=True, index=True)
    date_of_birth = Column(Date)
    annual_income = Column(Float, nullable=True)
    credit_score = Column(Integer, nullable=True)
    employer_name = Column(String, nullable=True)
    employer_address = Column(String, nullable=True)
    job_title = Column(String, nullable=True)
    employment_start_date = Column(Date, nullable=True)
    account_statement_ref = Column(String, nullable=True) # Reference to object storage

    applications = relationship("Application", back_populates="applicant")

class Application(Base):
    __tablename__ = "applications"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    applicant_id = Column(String, ForeignKey("applicants.id"))
    credit_card_offer_id = Column(String, ForeignKey("credit_card_offers.id"))
    status = Column(String, default="Pending") # e.g., Pending, Approved, Rejected
    submission_date = Column(Date)

    applicant = relationship("Applicant", back_populates="applications")
    credit_card_offer = relationship("CreditCardOffer", back_populates="applications")
