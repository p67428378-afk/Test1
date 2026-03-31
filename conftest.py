import pytest
from app import create_app
from database import db, User, bcrypt
from config import Config

class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory:'
    TESTING = True
    WTF_CSRF_ENABLED = False

@pytest.fixture(scope='module')
def app():
    app = create_app()
    app.config.from_object(TestConfig)
    with app.app_context():
        db.create_all()
        yield app
        db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def session(app):
    with app.app_context():
        # Establish a nested session for the test
        db.session.begin_nested()
        yield db.session
        db.session.rollback() # Rollback the nested transaction
        db.session.remove() # Remove the session

@pytest.fixture(scope='function')
def create_user(session):
    from database import User # Explicit import
    def _create_user(name, email, password):
        user = User(name=name, email=email)
        user.set_password(password)
        session.add(user)
        session.commit()
        return user
    return _create_user
