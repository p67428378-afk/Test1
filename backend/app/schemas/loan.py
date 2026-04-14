from pydantic import BaseModel, ConfigDict

class LoanBase(BaseModel):
    amount: float
    loan_type: str

class LoanCreate(LoanBase):
    pass

class Loan(LoanBase):
    id: int
    owner_id: int
    status: str
    model_config = ConfigDict(from_attributes=True)
