
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from sqlalchemy.pool import StaticPool
import os

# Use in-memory SQLite for testing, or a real DB if DATABASE_URL is set
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")

# For in-memory SQLite, use StaticPool to ensure the same connection is used across requests
# This is crucial for tests where tables are created and dropped per test function
if DATABASE_URL == "sqlite:///:memory:":
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        poolclass=StaticPool,
    )
else:
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
