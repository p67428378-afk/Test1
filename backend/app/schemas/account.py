from pydantic import BaseModel, ConfigDict

class AccountBase(BaseModel):
    balance: float
    account_type: str

class AccountCreate(AccountBase):
    pass

class Account(AccountBase):
    id: int
    owner_id: int
    model_config = ConfigDict(from_attributes=True)
