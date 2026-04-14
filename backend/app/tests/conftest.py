import pytest
from fastapi.testclient import TestClient
import mongomock_motor

from app.main import app
from app.database import get_database


@pytest.fixture(scope="module")
def client():
    # Set up a mock database for testing
    mock_client = mongomock_motor.AsyncMongoMockClient()
    db = mock_client.testdb

    def override_get_database():
        return db

    app.dependency_overrides[get_database] = override_get_database

    with TestClient(app) as c:
        # Add the mock db to the app state so it can be accessed in tests
        c.app.mongodb = db
        yield c

    # Clean up the dependency override
    app.dependency_overrides.clear()
