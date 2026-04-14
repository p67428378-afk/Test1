from pydantic import BaseModel, ConfigDict

class DepositBase(BaseModel):
    amount: float
    deposit_type: str

class DepositCreate(DepositBase):
    pass

class Deposit(DepositBase):
    id: int
    account_id: int
    status: str
    model_config = ConfigDict(from_attributes=True)
