
import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.pool import StaticPool
from fastapi.testclient import TestClient
import os

from backend.main import app
from backend.database import get_db
from backend.models import Base as AppBase

DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///:memory:")

@pytest.fixture(name="session")
def session_fixture():
    if DATABASE_URL == "sqlite:///:memory:":
        engine = create_engine(
            DATABASE_URL,
            connect_args={"check_same_thread": False},
            poolclass=StaticPool,
        )
    else:
        engine = create_engine(DATABASE_URL)

    AppBase.metadata.create_all(bind=engine)

    TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine, expire_on_commit=False)

    with TestingSessionLocal() as session:
        yield session
    
    AppBase.metadata.drop_all(bind=engine)


@pytest.fixture(name="client")
def client_fixture(session):
    def override_get_db():
        yield session

    app.dependency_overrides[get_db] = override_get_db
    with TestClient(app) as client:
        yield client
    app.dependency_overrides.clear()
