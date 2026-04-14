from pydantic_settings import BaseSettings
from pydantic import ConfigDict

class Settings(BaseSettings):
    SECRET_KEY: str
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    MONGO_DETAILS: str

    model_config = ConfigDict(env_file=".env")

settings = Settings()
