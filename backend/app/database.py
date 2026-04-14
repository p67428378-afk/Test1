from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from app.core.config import settings

def get_client() -> AsyncIOMotorClient:
    return AsyncIOMotorClient(settings.MONGO_DETAILS)

def get_database() -> AsyncIOMotorDatabase:
    client = get_client()
    return client.cab_management
