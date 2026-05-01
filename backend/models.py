from sqlalchemy import Column, Integer, String, Float, ForeignKey, Date
from sqlalchemy.orm import relationship
from .database import Base
import uuid

class Customer(Base):
    __tablename__ = "customers"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    name = Column(String, index=True)
    email = Column(String, unique=True, index=True)
    phone = Column(String)

    policies = relationship("Policy", back_populates="customer")

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    vin = Column(String, unique=True, index=True)
    make = Column(String)
    model = Column(String)
    year = Column(Integer)
    engine_size_cc = Column(Integer)

    policies = relationship("Policy", back_populates="vehicle")

class Policy(Base):
    __tablename__ = "policies"

    id = Column(String, primary_key=True, index=True, default=lambda: str(uuid.uuid4()))
    customer_id = Column(String, ForeignKey("customers.id"))
    vehicle_id = Column(String, ForeignKey("vehicles.id"))
    base_premium = Column(Float)
    ncb_years = Column(Integer)
    ncb_discount_percentage = Column(Float)
    vehicle_multiplier = Column(Float)
    final_premium = Column(Float)
    created_date = Column(Date)
    last_updated_date = Column(Date)

    customer = relationship("Customer", back_populates="policies")
    vehicle = relationship("Vehicle", back_populates="policies")
