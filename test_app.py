import json

def test_register_user_success(client, session):
    response = client.post(
        '/register',
        data=json.dumps({'name': 'Test User', 'email': 'test@example.com', 'password': 'password123'}),
        content_type='application/json'
    )
    assert response.status_code == 201
    assert 'User registered successfully' in response.json['message']

def test_register_user_missing_fields(client):
    response = client.post(
        '/register',
        data=json.dumps({'name': 'Test User', 'email': 'test@example.com'}),
        content_type='application/json'
    )
    assert response.status_code == 400
    assert 'Name, email, and password are required' in response.json['error']

def test_register_user_already_exists(client, session):
    # Register once
    client.post(
        '/register',
        data=json.dumps({'name': 'Test User', 'email': 'existing@example.com', 'password': 'password123'}),
        content_type='application/json'
    )
    # Try to register again with the same email
    response = client.post(
        '/register',
        data=json.dumps({'name': 'Another User', 'email': 'existing@example.com', 'password': 'anotherpass'}),
        content_type='application/json'
    )
    assert response.status_code == 409
    assert 'Email already registered' in response.json['error']
