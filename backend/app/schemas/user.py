from pydantic import BaseModel, EmailStr, ConfigDict

class UserBase(BaseModel):
    email: EmailStr

class UserCreate(UserBase):
    password: str

class UserInDB(UserBase):
    hashed_password: str

    model_config = ConfigDict(from_attributes=True)

class User(UserBase):
    model_config = ConfigDict(from_attributes=True)
