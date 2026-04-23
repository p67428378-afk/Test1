
from sqlalchemy import Column, String, Enum
from ..db.database import Base
import enum

class TransferStatus(str, enum.Enum):
    PENDING = "PENDING"
    CANCELLED = "CANCELLED"
    EXECUTED = "EXECUTED"
    FAILED = "FAILED"

class Cancellation(Base):
    __tablename__ = "cancellations"

    cancellationId = Column(String, primary_key=True, index=True)
    transferReferenceId = Column(String, index=True, unique=True)
    accountNumber = Column(String)
    status = Column(Enum(TransferStatus))
    reason = Column(String, nullable=True)
