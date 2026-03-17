from sqlalchemy import Column, Integer, String, Date, Numeric, Boolean, ForeignKey
from sqlalchemy.orm import relationship
from .database import Base, settings
from cryptography.fernet import Fernet
import base64

# Generate a key for Fernet encryption. In a real application, this should be securely managed.
# For demonstration, we'll use the SECRET_KEY from settings.
# The key must be 32 url-safe base64-encoded bytes.
# Fernet.generate_key() can be used to generate a new key.

# Ensure the SECRET_KEY is 32 bytes for AES-256, then base64 encode it for Fernet
# If settings.SECRET_KEY is not 32 bytes, Fernet will raise an error.
# For simplicity, we assume settings.SECRET_KEY is already a suitable 32-byte string
# or can be padded/truncated. For production, generate a proper Fernet key.

# For now, let's ensure the key is correctly formatted for Fernet
try:
    fernet_key = base64.urlsafe_b64encode(settings.SECRET_KEY.encode('utf-8').ljust(32)[:32])
    f = Fernet(fernet_key)
except Exception as e:
    print(f"Error initializing Fernet: {e}. Ensure SECRET_KEY is valid.")
    # Fallback or raise error, depending on desired behavior
    fernet_key = Fernet.generate_key() # Generate a new key if the provided one is invalid
    f = Fernet(fernet_key)
    print("Using a newly generated Fernet key. Please update your .env with a secure key.")

def encrypt_data(data: str) -> str:
    if data is None:
        return None
    return f.encrypt(data.encode()).decode()

def decrypt_data(data: str) -> str:
    if data is None:
        return None
    try:
        return f.decrypt(data.encode()).decode()
    except Exception:
        return "[Decryption Error]"

class Applicant(Base):
    __tablename__ = "applicants"

    applicant_id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String, index=True)
    last_name = Column(String, index=True)
    date_of_birth = Column(Date)
    _ssn = Column("ssn", String) # Storing encrypted SSN
    email = Column(String, unique=True, index=True)
    phone_number = Column(String)
    address = Column(String)

    employment = relationship("Employment", back_populates="applicant", uselist=False)
    bank_account = relationship("BankAccount", back_populates="applicant", uselist=False)
    loan_application = relationship("LoanApplication", back_populates="applicant", uselist=False)
    legal_declaration = relationship("LegalDeclaration", back_populates="applicant", uselist=False)

    @property
    def ssn(self):
        return decrypt_data(self._ssn)

    @ssn.setter
    def ssn(self, value: str):
        self._ssn = encrypt_data(value)

class Employment(Base):
    __tablename__ = "employment"

    employment_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"))
    company_name = Column(String)
    company_address = Column(String)
    job_title = Column(String)
    income = Column(Numeric(10, 2))

    applicant = relationship("Applicant", back_populates="employment")

class BankAccount(Base):
    __tablename__ = "bank_accounts"

    bank_account_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"))
    _account_number = Column("account_number", String) # Storing encrypted account number
    _aba_routing_number = Column("aba_routing_number", String) # Storing encrypted ABA routing number

    applicant = relationship("Applicant", back_populates="bank_account")

    @property
    def account_number(self):
        return decrypt_data(self._account_number)

    @account_number.setter
    def account_number(self, value: str):
        self._account_number = encrypt_data(value)

    @property
    def aba_routing_number(self):
        return decrypt_data(self._aba_routing_number)

    @aba_routing_number.setter
    def aba_routing_number(self, value: str):
        self._aba_routing_number = encrypt_data(value)

class LoanApplication(Base):
    __tablename__ = "loan_applications"

    application_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"))
    loan_purpose = Column(String)
    loan_amount = Column(Numeric(10, 2))
    loan_period_months = Column(Integer)
    submission_date = Column(Date)
    status = Column(String, default="Submitted")

    applicant = relationship("Applicant", back_populates="loan_application")

class LegalDeclaration(Base):
    __tablename__ = "legal_declarations"

    legal_id = Column(Integer, primary_key=True, index=True)
    applicant_id = Column(Integer, ForeignKey("applicants.applicant_id"))
    citizenship_status = Column(String)
    has_pending_cases = Column(Boolean)
    declaration_date = Column(Date)

    applicant = relationship("Applicant", back_populates="legal_declaration")
