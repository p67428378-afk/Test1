from fastapi.testclient import TestClient

def test_calculate_premium_success(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "vehicle_type": "SUV",
        "no_claims_bonus_percentage": 0.3,
        "vehicle_multiplier": 1.2
    })
    assert response.status_code == 200
    data = response.json()
    assert data["calculated_premium"] == 420.0
    assert data["policy_details"]["vehicle_type"] == "SUV"
    assert data["policy_details"]["no_claims_bonus_percentage"] == 0.3
    assert data["policy_details"]["vehicle_multiplier"] == 1.2
    assert data["policy_details"]["base_premium"] == 500.0

def test_calculate_premium_invalid_ncb(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "vehicle_type": "SUV",
        "no_claims_bonus_percentage": 0.6,
        "vehicle_multiplier": 1.2
    })
    assert response.status_code == 422

def test_calculate_premium_invalid_multiplier(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "vehicle_type": "SUV",
        "no_claims_bonus_percentage": 0.3,
        "vehicle_multiplier": 2.0
    })
    assert response.status_code == 422
