from pydantic import BaseModel, EmailStr, Field, ConfigDict
from typing import Optional
from datetime import datetime

class UserModel(BaseModel):
    id: str = Field(default_factory=str, alias="_id")
    email: EmailStr
    hashed_password: str
    failed_login_attempts: int = 0
    account_locked_until: Optional[datetime] = None

    model_config = ConfigDict(
        populate_by_name=True,
        arbitrary_types_allowed=True,
    )
