from fastapi.testclient import TestClient
from app import app

client = TestClient(app)

def test_read_profile_success():
    response = client.get("/profile/1")
    assert response.status_code == 200
    assert response.json() == {"user_id": 1, "name": "John Doe"}

def test_read_profile_not_found():
    response = client.get("/profile/999")
    assert response.status_code == 404
    assert response.json() == {"detail": "User not found"}
