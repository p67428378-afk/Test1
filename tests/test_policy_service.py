
import pytest
from sqlalchemy.orm import Session
from backend.app.services.policy_service import PolicyService
from backend import models, schemas

@pytest.fixture
def policy_service():
    return PolicyService()

def test_create_policy(session: Session, policy_service: PolicyService):
    # Create a customer and vehicle
    customer = models.Customer(name="Test Customer", email="test@example.com", phone="1234567890")
    vehicle = models.Vehicle(vin="TESTVIN123", make="TestMake", model="TestModel", year=2023, engine_size_cc=2000)
    session.add(customer)
    session.add(vehicle)
    session.commit()
    session.refresh(customer)
    session.refresh(vehicle)

    policy_schema = schemas.Policy(
        customer=schemas.Customer.model_validate(customer),
        vehicle=schemas.Vehicle.model_validate(vehicle),
        base_premium=500.0,
        ncb_years=2,
        ncb_discount_percentage=0.3,
        vehicle_multiplier=1.0,
        final_premium=350.0,
    )

    created_policy = policy_service.create_policy(db=session, policy=policy_schema)

    assert created_policy is not None
    assert created_policy.customer_id == customer.id
    assert created_policy.vehicle_id == vehicle.id
    assert created_policy.final_premium == 350.0
