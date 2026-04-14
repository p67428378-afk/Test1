from datetime import datetime, timedelta
from typing import Optional

from app.core.security import get_password_hash, verify_password
from app.models.user import UserModel
from app.database import AsyncIOMotorDatabase


async def get_user(db: AsyncIOMotorDatabase, email: str) -> Optional[UserModel]:
    user = await db.users.find_one({"email": email})
    if user:
        user["_id"] = str(user["_id"])
        return UserModel(**user)
    return None


async def authenticate_user(db: AsyncIOMotorDatabase, email: str, password: str) -> Optional[UserModel]:
    user = await get_user(db, email)
    if not user:
        return None

    if user.account_locked_until and user.account_locked_until > datetime.utcnow():
        return user

    if not verify_password(password, user.hashed_password):
        await db.users.update_one(
            {"email": email},
            {"$inc": {"failed_login_attempts": 1}, "$set": {"last_login_attempt": datetime.utcnow()}}
        )
        if user.failed_login_attempts + 1 >= 5:
            await db.users.update_one(
                {"email": email},
                {"$set": {"account_locked_until": datetime.utcnow() + timedelta(minutes=15)}}
            )
        return None

    await db.users.update_one(
        {"email": email},
        {"$set": {"failed_login_attempts": 0, "last_login_attempt": datetime.utcnow(), "account_locked_until": None}}
    )

    return user
