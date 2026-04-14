from fastapi.testclient import TestClient

def test_create_loan(client: TestClient):
    # First, create a user
    user_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    assert user_response.status_code == 200
    user_id = user_response.json()["id"]

    # Then, create a loan for the user
    response = client.post(f"/loans/?user_id={user_id}", json={"amount": 10000.0, "loan_type": "personal"})
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 10000.0
    assert data["loan_type"] == "personal"
    assert data["owner_id"] == user_id
    assert data["status"] == "pending"

def test_read_loan(client: TestClient):
    # First, create a user and a loan
    user_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    user_id = user_response.json()["id"]
    loan_response = client.post(f"/loans/?user_id={user_id}", json={"amount": 10000.0, "loan_type": "personal"})
    loan_id = loan_response.json()["id"]

    # Then, read the loan
    response = client.get(f"/loans/{loan_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == loan_id
    assert data["amount"] == 10000.0
    assert data["loan_type"] == "personal"
    assert data["owner_id"] == user_id
