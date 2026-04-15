from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from app.db.database import Base
import uuid

class Policy(Base):
    __tablename__ = "policies"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    policyholder_id = Column(String, ForeignKey("policyholders.id"))
    vehicle_id = Column(String, ForeignKey("vehicles.id"))
    base_rate = Column(Float)
    ncb_years = Column(Integer)
    calculated_premium = Column(Float)
    start_date = Column(Date)
    end_date = Column(Date)

    policyholder = relationship("Policyholder")
    vehicle = relationship("Vehicle")

class Policyholder(Base):
    __tablename__ = "policyholders"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    address = Column(String)
    contact_info = Column(String)

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    type = Column(String)
    risk_factor = Column(Float)
