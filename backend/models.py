from sqlalchemy import Column, Float, Integer, String
from .database import Base

class Policy(Base):
    __tablename__ = "policies"

    id = Column(Integer, primary_key=True, index=True)
    ncb_level = Column(String, index=True)
    vehicle_id = Column(Integer, index=True)

class Vehicle(Base):
    __tablename__ = "vehicles"

    id = Column(Integer, primary_key=True, index=True)
    make = Column(String, index=True)
    model = Column(String, index=True)
    year = Column(Integer, index=True)
    type = Column(String, index=True)

class NCBTierRules(Base):
    __tablename__ = "ncb_tier_rules"

    id = Column(Integer, primary_key=True, index=True)
    ncb_level = Column(String, unique=True, index=True)
    discount_percentage = Column(Float, index=True)

class VehicleMultiplierRules(Base):
    __tablename__ = "vehicle_multiplier_rules"

    id = Column(Integer, primary_key=True, index=True)
    vehicle_type = Column(String, index=True)
    vehicle_age_min = Column(Integer, index=True)
    vehicle_age_max = Column(Integer, index=True)
    multiplier_value = Column(Float, index=True)
