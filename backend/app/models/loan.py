from sqlalchemy import Column, Integer, String, Float, ForeignKey
from sqlalchemy.orm import relationship

from ..db.database import Base

class Loan(Base):
    __tablename__ = "loans"

    id = Column(Integer, primary_key=True, index=True)
    amount = Column(Float)
    loan_type = Column(String)
    status = Column(String, default="pending")
    owner_id = Column(Integer, ForeignKey("users.id"))

    owner = relationship("User")
