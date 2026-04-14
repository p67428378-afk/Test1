from fastapi.testclient import TestClient

def test_create_account(client: TestClient):
    # First, create a user
    user_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    assert user_response.status_code == 200
    user_id = user_response.json()["id"]

    # Then, create an account for the user
    response = client.post(f"/accounts/?user_id={user_id}", json={"balance": 1000.0, "account_type": "checking"})
    assert response.status_code == 200
    data = response.json()
    assert data["balance"] == 1000.0
    assert data["account_type"] == "checking"
    assert data["owner_id"] == user_id

def test_read_account(client: TestClient):
    # First, create a user and an account
    user_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    user_id = user_response.json()["id"]
    account_response = client.post(f"/accounts/?user_id={user_id}", json={"balance": 1000.0, "account_type": "checking"})
    account_id = account_response.json()["id"]

    # Then, read the account
    response = client.get(f"/accounts/{account_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == account_id
    assert data["balance"] == 1000.0
    assert data["account_type"] == "checking"
    assert data["owner_id"] == user_id
