import os
from sqlalchemy import create_engine, Column, Integer, String, Text, DateTime, Boolean, ForeignKey, Enum
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime
import enum
from dotenv import load_dotenv

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL", "postgresql://user:password@host:port/database_name")

Base = declarative_base()

class ApplicationStatus(enum.Enum):
    PENDING = "Pending"
    APPROVED = "Approved"
    REJECTED = "Rejected"

class Applicant(Base):
    __tablename__ = 'applicants'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    phone_number = Column(String)
    date_of_birth = Column(DateTime)
    address = Column(Text)
    # Add other personal details as needed

    applications = relationship("LoanApplication", back_populates="applicant")

class LoanApplication(Base):
    __tablename__ = 'loan_applications'
    id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey('applicants.id'), nullable=False)
    loan_amount = Column(Integer, nullable=False)
    loan_tenure = ColumnInteger, nullable=False)
    application_date = Column(DateTime, default=datetime.utcnow)
    status = Column(Enum(ApplicationStatus), default=ApplicationStatus.PENDING, nullable=False)
    financial_details = Column(Text) # Income, EmploymentStatus, Liabilities (can be JSON or structured text)
    bank_details = Column(Text)      # BankName, AccountNumber, IFSC/SWIFT (can be JSON or structured text)
    legal_consent = Column(Boolean, default=False)
    legal_consent_timestamp = Column(DateTime)
    # Add other loan-specific details as needed

    applicant = relationship("Applicant", back_populates="applications")
    reviews = relationship("ApplicationReview", back_populates="loan_application")

class LoanOfficer(Base):
    __tablename__ = 'loan_officers'
    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, nullable=False)
    last_name = Column(String, nullable=False)
    email = Column(String, unique=True, index=True, nullable=False)
    role = Column(String, default="Officer")

    reviews = relationship("ApplicationReview", back_populates="loan_officer")

class ApplicationReview(Base):
    __tablename__ = 'application_reviews'
    id = Column(Integer, primary_key=True, index=True)
    application_id = Column(Integer, ForeignKey('loan_applications.id'), nullable=False)
    officer_id = Column(Integer, ForeignKey('loan_officers.id'), nullable=False)
    review_date = Column(DateTime, default=datetime.utcnow)
    decision = Column(Enum(ApplicationStatus), nullable=False) # APPROVED or REJECTED
    comments = Column(Text)

    loan_application = relationship("LoanApplication", back_populates="reviews")
    loan_officer = relationship("LoanOfficer", back_populates="reviews")

# Database initialization
def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database tables created or already exist.")
    return engine

# Session Local for dependency injection
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=init_db())

# Helper to get database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

if __name__ == "__main__":
    # This block will run when database.py is executed directly
    # It ensures the tables are created when the script is run.
    engine = init_db()
    print(f"Connected to database: {DATABASE_URL}")
    # Example of adding a dummy loan officer if needed
    # with SessionLocal() as db:
    #     if not db.query(LoanOfficer).filter_by(email="loan.officer@example.com").first():
    #         officer = LoanOfficer(first_name="Loan", last_name="Officer", email="loan.officer@example.com")
    #         db.add(officer)
    #         db.commit()
    #         print("Dummy loan officer added.")
