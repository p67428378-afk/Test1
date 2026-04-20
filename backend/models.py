from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Enum, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    hashed_password = Column(String)
    role = Column(String, default="user")

class MembershipCategory(str, enum.Enum):
    owner = "owner"
    joint_owner = "joint_owner"

class Member(Base):
    __tablename__ = "members"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    address = Column(String)
    contact_details = Column(String)
    email = Column(String, unique=True, index=True)
    aadhaar_pan = Column(String)
    membership_category = Column(Enum(MembershipCategory))
    status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

class Property(Base):
    __tablename__ = "properties"

    id = Column(Integer, primary_key=True, index=True)
    flat_number = Column(String)
    tower_unit_code = Column(String)
    area = Column(Float)
    current_owner_member_id = Column(Integer, ForeignKey("members.id"))
    previous_owner_member_id = Column(Integer, ForeignKey("members.id"))
    share_certificate_number = Column(String)
    legal_status = Column(String)
    dues_status = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())

    current_owner = relationship("Member", foreign_keys=[current_owner_member_id])
    previous_owner = relationship("Member", foreign_keys=[previous_owner_member_id])

class TransactionType(str, enum.Enum):
    resale = "resale"
    first_time_purchase = "first_time_purchase"
    gift = "gift"
    transfer_between_members = "transfer_between_members"

class RequestStatus(str, enum.Enum):
    initiated = "initiated"
    docs_pending = "docs_pending"
    docs_verified = "docs_verified"
    payment_pending = "payment_pending"
    payment_verified = "payment_verified"
    approved = "approved"
    rejected = "rejected"
    closed = "closed"

class FlatTransferRequest(Base):
    __tablename__ = "flat_transfer_requests"

    id = Column(Integer, primary_key=True, index=True)
    buyer_id = Column(Integer, ForeignKey("members.id"))
    seller_id = Column(Integer, ForeignKey("members.id"))
    flat_id = Column(Integer, ForeignKey("properties.id"))
    transaction_type = Column(Enum(TransactionType))
    request_status = Column(Enum(RequestStatus), default=RequestStatus.initiated)
    initiated_by = Column(Integer, ForeignKey("users.id"))
    initiated_at = Column(DateTime(timezone=True), server_default=func.now())
    approved_by = Column(Integer, ForeignKey("users.id"))
    approved_at = Column(DateTime(timezone=True))
    application_number = Column(String, unique=True)

    buyer = relationship("Member", foreign_keys=[buyer_id])
    seller = relationship("Member", foreign_keys=[seller_id])
    flat = relationship("Property")
    initiator = relationship("User", foreign_keys=[initiated_by])
    approver = relationship("User", foreign_keys=[approved_by])

class DocumentStatus(str, enum.Enum):
    pending = "pending"
    verified = "verified"
    rejected = "rejected"

class Document(Base):
    __tablename__ = "documents"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("flat_transfer_requests.id"))
    document_type = Column(String)
    file_path_url = Column(String)
    uploaded_by = Column(Integer, ForeignKey("users.id"))
    uploaded_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(Enum(DocumentStatus), default=DocumentStatus.pending)
    remarks = Column(String)

    request = relationship("FlatTransferRequest")
    uploader = relationship("User")

class FinancialTransactionType(str, enum.Enum):
    fee = "fee"
    dues = "dues"

class FinancialTransaction(Base):
    __tablename__ = "financial_transactions"

    id = Column(Integer, primary_key=True, index=True)
    request_id = Column(Integer, ForeignKey("flat_transfer_requests.id"))
    amount = Column(Float)
    transaction_type = Column(Enum(FinancialTransactionType))
    payment_mode = Column(String)
    due_date = Column(DateTime(timezone=True))
    payment_date = Column(DateTime(timezone=True))
    bank_reference = Column(String)
    received_by = Column(Integer, ForeignKey("users.id"))
    status = Column(String)

    request = relationship("FlatTransferRequest")
    receiver = relationship("User")

class AuditLog(Base):
    __tablename__ = "audit_logs"

    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    action = Column(String)
    entity_type = Column(String)
    entity_id = Column(Integer)
    old_value = Column(String)
    new_value = Column(String)
    timestamp = Column(DateTime(timezone=True), server_default=func.now())

    user = relationship("User")
