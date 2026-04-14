from fastapi.testclient import TestClient

def test_create_user(client: TestClient):
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 200
    data = response.json()
    assert data["email"] == "test@example.com"
    assert "id" in data
    assert "is_active" in data
    assert "hashed_password" not in data

def test_create_user_existing_email(client: TestClient):
    client.post(
        "/users/",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": "testpassword"},
    )
    assert response.status_code == 400
    assert response.json() == {"detail": "Email already registered"}

def test_create_user_empty_password(client: TestClient):
    response = client.post(
        "/users/",
        json={"email": "test@example.com", "password": ""},
    )
    assert response.status_code == 422
