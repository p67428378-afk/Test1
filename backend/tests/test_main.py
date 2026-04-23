from fastapi.testclient import TestClient

def test_base_premium_calculation(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 0,
        "vehicle_risk_factor": 1.0,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    assert data["calculated_premium"] == 500.0
    assert "policy_id" in data

def test_ncb_discount_1_year(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 1,
        "vehicle_risk_factor": 1.0,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    # 500 * (1 - 0.20) = 400
    assert data["calculated_premium"] == 400.0

def test_ncb_discount_5_years(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 5,
        "vehicle_risk_factor": 1.0,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    # 500 * (1 - 0.50) = 250
    assert data["calculated_premium"] == 250.0

def test_ncb_discount_capped_at_5_years(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 6,
        "vehicle_risk_factor": 1.0,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    # 500 * (1 - 0.50) = 250
    assert data["calculated_premium"] == 250.0

def test_vehicle_multiplier_low(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 0,
        "vehicle_risk_factor": 0.8,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    # 500 * 0.8 = 400
    assert data["calculated_premium"] == 400.0

def test_vehicle_multiplier_high(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 0,
        "vehicle_risk_factor": 1.6,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    # 500 * 1.6 = 800
    assert data["calculated_premium"] == 800.0

def test_combined_ncb_and_multiplier(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 3,
        "vehicle_risk_factor": 1.2,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 200
    data = response.json()
    # 500 * (1 - 0.4) * 1.2 = 300 * 1.2 = 360
    # My formula for NCB is 0.10 * years + 0.10, so for 3 years it's 0.40
    assert abs(data["calculated_premium"] - 360.0) < 0.01

def test_invalid_ncb_years(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": -1,
        "vehicle_risk_factor": 1.0,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 400

def test_invalid_risk_factor_low(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 0,
        "vehicle_risk_factor": 0.7,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 400

def test_invalid_risk_factor_high(client: TestClient):
    response = client.post("/api/v1/insurance/premium", json={
        "ncb_years": 0,
        "vehicle_risk_factor": 1.7,
        "policy_holder_name": "Test User",
        "vehicle_type": "Sedan"
    })
    assert response.status_code == 400
