from fastapi.testclient import TestClient

def test_create_deposit(client: TestClient):
    # First, create a user and an account
    user_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    user_id = user_response.json()["id"]
    account_response = client.post(f"/accounts/?user_id={user_id}", json={"balance": 1000.0, "account_type": "checking"})
    account_id = account_response.json()["id"]

    # Then, create a deposit for the account
    response = client.post(f"/deposits/?account_id={account_id}", json={"amount": 500.0, "deposit_type": "check"})
    assert response.status_code == 200
    data = response.json()
    assert data["amount"] == 500.0
    assert data["deposit_type"] == "check"
    assert data["account_id"] == account_id
    assert data["status"] == "pending"

def test_read_deposit(client: TestClient):
    # First, create a user, an account, and a deposit
    user_response = client.post("/users/", json={"email": "test@example.com", "password": "testpassword"})
    user_id = user_response.json()["id"]
    account_response = client.post(f"/accounts/?user_id={user_id}", json={"balance": 1000.0, "account_type": "checking"})
    account_id = account_response.json()["id"]
    deposit_response = client.post(f"/deposits/?account_id={account_id}", json={"amount": 500.0, "deposit_type": "check"})
    deposit_id = deposit_response.json()["id"]

    # Then, read the deposit
    response = client.get(f"/deposits/{deposit_id}")
    assert response.status_code == 200
    data = response.json()
    assert data["id"] == deposit_id
    assert data["amount"] == 500.0
    assert data["deposit_type"] == "check"
    assert data["account_id"] == account_id
