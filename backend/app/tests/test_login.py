import pytest
from fastapi.testclient import TestClient
from faker import Faker

from app.core.security import get_password_hash

fake = Faker()

@pytest.mark.asyncio
async def test_login_success(client: TestClient):
    email = fake.email()
    password = fake.password()
    hashed_password = get_password_hash(password)

    # Create a user in the mock database
    user_collection = client.app.mongodb.users
    await user_collection.insert_one({"email": email, "hashed_password": hashed_password, "failed_login_attempts": 0, "account_locked_until": None})

    response = client.post("/api/auth/login", data={"username": email, "password": password})

    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

@pytest.mark.asyncio
async def test_login_wrong_password(client: TestClient):
    email = fake.email()
    password = fake.password()
    wrong_password = fake.password()
    hashed_password = get_password_hash(password)

    user_collection = client.app.mongodb.users
    await user_collection.insert_one({"email": email, "hashed_password": hashed_password, "failed_login_attempts": 0, "account_locked_until": None})

    response = client.post("/api/auth/login", data={"username": email, "password": wrong_password})

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid email or password"

@pytest.mark.asyncio
async def test_login_wrong_email(client: TestClient):
    email = fake.email()
    password = fake.password()

    response = client.post("/api/auth/login", data={"username": email, "password": password})

    assert response.status_code == 401
    data = response.json()
    assert data["detail"] == "Invalid email or password"

@pytest.mark.asyncio
async def test_account_lockout(client: TestClient):
    email = fake.email()
    password = fake.password()
    wrong_password = fake.password()
    hashed_password = get_password_hash(password)

    user_collection = client.app.mongodb.users
    await user_collection.insert_one({"email": email, "hashed_password": hashed_password, "failed_login_attempts": 0, "account_locked_until": None})

    for _ in range(5):
        response = client.post("/api/auth/login", data={"username": email, "password": wrong_password})
        assert response.status_code == 401

    response = client.post("/api/auth/login", data={"username": email, "password": password})
    assert response.status_code == 401
    data = response.json()
    assert "Account locked" in data["detail"]

@pytest.mark.asyncio
async def test_access_protected_route_with_token(client: TestClient):
    email = fake.email()
    password = fake.password()
    hashed_password = get_password_hash(password)

    user_collection = client.app.mongodb.users
    await user_collection.insert_one({"email": email, "hashed_password": hashed_password, "failed_login_attempts": 0, "account_locked_until": None})

    login_response = client.post("/api/auth/login", data={"username": email, "password": password})
    token = login_response.json()["access_token"]

    response = client.get("/api/users/me", headers={"Authorization": f"Bearer {token}"})
    assert response.status_code == 200
    assert response.json()["email"] == email

@pytest.mark.asyncio
async def test_access_protected_route_with_invalid_token(client: TestClient):
    response = client.get("/api/users/me", headers={"Authorization": "Bearer invalidtoken"})
    assert response.status_code == 401
    assert response.json()["detail"] == "Could not validate credentials"

@pytest.mark.asyncio
async def test_access_protected_route_without_token(client: TestClient):
    response = client.get("/api/users/me")
    assert response.status_code == 401
    assert response.json()["detail"] == "Not authenticated"
