from pydantic import BaseModel, EmailStr, Field

class UserBase(BaseModel):
    # Use EmailStr to automatically validate email format.
    email: EmailStr

class UserCreate(UserBase):
    # Use Field to enforce a minimum password length of 8 characters.
    password: str = Field(..., min_length=8)

class User(UserBase):
    id: int

    class Config:
        from_attributes = True
