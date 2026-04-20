from fastapi.testclient import TestClient
from sqlalchemy.orm import Session
from backend import models

def test_register_user(client: TestClient):
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "role" in data

def test_register_existing_user(client: TestClient):
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    response = client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_login_for_access_token(client: TestClient):
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert "access_token" in data
    assert data["token_type"] == "bearer"

def test_login_with_wrong_password(client: TestClient):
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    response = client.post(
        "/auth/token",
        data={"username": "test@example.com", "password": "wrongpassword"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}

def test_login_with_wrong_username(client: TestClient):
    client.post(
        "/auth/register",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    response = client.post(
        "/auth/token",
        data={"username": "wrong@example.com", "password": "testpassword"},
    )
    assert response.status_code == 401
    assert response.json() == {"detail": "Incorrect username or password"}
