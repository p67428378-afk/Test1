import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from backend.database import Base, get_db
from backend import crud, schemas, models
from backend.main import app

SQLALCHEMY_DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
TestingSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


Base.metadata.create_all(bind=engine)


def override_get_db():
    try:
        db = TestingSessionLocal()
        yield db
    finally:
        db.close()


app.dependency_overrides[get_db] = override_get_db


@pytest.fixture(scope="function")
def db_session():
    Base.metadata.create_all(bind=engine)
    db = TestingSessionLocal()
    yield db
    db.close()
    Base.metadata.drop_all(bind=engine)


def test_create_policy(db_session):
    customer = models.Customer(name="Test Customer", email="test@example.com", phone="1234567890")
    vehicle = models.Vehicle(vin="TESTVIN123", make="Test Make", model="Test Model", year=2023, engine_size_cc=2000)
    db_session.add(customer)
    db_session.add(vehicle)
    db_session.commit()

    policy_data = schemas.Policy(
        customer=customer,
        vehicle=vehicle,
        base_premium=500.0,
        ncb_years=2,
        ncb_discount_percentage=0.3,
        vehicle_multiplier=1.0,
        final_premium=350.0,
    )

    db_policy = crud.create_policy(db_session, policy_data)

    assert db_policy.id is not None
    assert db_policy.customer_id == customer.id
    assert db_policy.vehicle_id == vehicle.id
    assert db_policy.final_premium == 350.0
