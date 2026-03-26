from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from app.database import Base
import uuid

class Policyholder(Base):
    __tablename__ = "policyholders"

    policyholder_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    date_of_birth = Column(Date)
    address = Column(String)
    contact_info = Column(String)
    ssn = Column(String)  # Encrypted SSN
    medical_history = Column(String)  # Encrypted medical history reference or data

    policies = relationship("Policy", back_populates="policyholder")

class Policy(Base):
    __tablename__ = "policies"

    policy_id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    policyholder_id = Column(String, ForeignKey("policyholders.policyholder_id"))
    policy_type = Column(String)
    start_date = Column(Date)
    end_date = Column(Date)
    coverage_details = Column(String)
    status = Column(String)

    policyholder = relationship("Policyholder", back_populates="policies")
