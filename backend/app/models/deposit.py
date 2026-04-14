from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..db.database import Base

class Deposit(Base):
    __tablename__ = "deposits"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    deposit_type = Column(String)
    status = Column(String, default="pending")
    account_id = Column(Integer, ForeignKey("accounts.id"))

    account = relationship("Account", back_populates="deposits")
