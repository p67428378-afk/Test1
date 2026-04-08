import pytest
from flask import Flask
from database import db as app_db, User, bcrypt
from app import create_app
from config import Config

@pytest.fixture(scope='session')
def app():
    app = create_app()
    app.config.from_object(Config)
    app.config['TESTING'] = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///:memory:'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    with app.app_context():
        app_db.create_all()
        yield app
        app_db.drop_all()

@pytest.fixture(scope='function')
def client(app):
    return app.test_client()

@pytest.fixture(scope='function')
def session(app):
    with app.app_context():
        connection = app_db.engine.connect()
        transaction = connection.begin()
        app_db.session.configure(bind=connection) # Configure the session to use the test connection
        yield app_db.session # Yield the configured session

        transaction.rollback()
        connection.close()
        app_db.session.remove() # Remove the session
