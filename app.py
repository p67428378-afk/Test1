from flask import Flask, request, jsonify
from config import Config
from database import db, bcrypt, User

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    bcrypt.init_app(app)

    @app.route('/register', methods=['POST'])
    def register():
        data = request.get_json()
        name = data.get('name')
        email = data.get('email')
        password = data.get('password')

        if not all([name, email, password]):
            return jsonify({'error': 'Name, email, and password are required'}), 400

        if User.query.filter_by(email=email).first():
            return jsonify({'error': 'Email already registered'}), 409

        new_user = User(name=name, email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        return jsonify({'message': 'User registered successfully'}), 200

    @app.route('/login', methods=['POST'])
    def login():
        data = request.get_json()
        email = data.get('email')
        password = data.get('password')

        if not all([email, password]):
            return jsonify({'error': 'Email and password are required'}), 400

        user = User.query.filter_by(email=email).first()

        if user and user.check_password(password):
            return jsonify({'message': 'Login successful'}), 200
        else:
            return jsonify({'error': 'Invalid email or password'}), 401

    @app.route('/profile/<int:user_id>', methods=['GET'])
    def get_profile(user_id):
        user = User.query.filter_by(name=user_id).first()

        if not user:
            return jsonify({'error': 'User not found'}), 404

        return jsonify({
            'user_id': user.id,
            'name': user.name,
            'email': user.email
        }), 200

    return app

if __name__ == '__main__':
    app = create_app()
    with app.app_context():
        db.create_all()
    app.run(debug=True)
