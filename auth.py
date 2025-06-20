from flask import Blueprint, request, jsonify, make_response
from app.models import db, User
import bcrypt
import jwt
from datetime import datetime, timedelta
from functools import wraps

auth_bp = Blueprint('auth_bp', __name__)

# Decorator untuk mengecek token
def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs): 
        token = request.cookies.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            from flask import current_app
            secret = current_app.config.get('SECRET_KEY', 'your_secret_key')
            data = jwt.decode(token, secret, algorithms=["HS256"])
            current_user = User.query.filter_by(user_id=data['user_id']).first()
        except Exception:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        roles = data['roles']  # roles: list, misal ['kaprodi', 'dosen'] atau ['dosen']

        # Validasi kaprodi hanya satu
        if 'kaprodi' in roles:
            existing_kaprodi = User.query.filter(User.roles.any('kaprodi')).first()
            if existing_kaprodi:
                return jsonify({'error': 'Role kaprodi sudah terpakai'}), 400
            # Kaprodi boleh merangkap dosen
        else:
            # Dosen hanya boleh satu role
            if len(roles) > 1 or roles[0] != 'dosen':
                return jsonify({'error': 'Role dosen hanya boleh satu dan tidak bisa merangkap'}), 400

        # Cek email/nip unik
        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already registered'}), 400
        if User.query.filter_by(nip=data['nip']).first():
            return jsonify({'error': 'NIP already registered'}), 400

        # Hash password
        hashed = bcrypt.hashpw(data['password'].encode('utf-8'), bcrypt.gensalt())
        new_user = User(
            nama=data['nama'],
            nip=data['nip'],
            email=data['email'],
            password_hash=hashed.decode('utf-8'),
            roles=roles
        )
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/login', methods=['POST'])
def login():
    try:
        data = request.json
        user = User.query.filter_by(nip=data['NIP']).first()
        if user and bcrypt.checkpw(data['password'].encode('utf-8'), user.password_hash.encode('utf-8')):
            from flask import current_app
            secret = current_app.config.get('SECRET_KEY', 'your_secret_key')
            token = jwt.encode({
                'user_id': user.user_id,
                'exp': datetime.utcnow() + timedelta(hours=24)
            }, secret, algorithm="HS256")
            response = make_response(jsonify({
                'message': 'Login successful',
                'user': {
                    'id': user.user_id,
                    'nama': user.nama,
                    'email': user.email,
                    'peran': user.peran
                }
            }))
            response.set_cookie('token', token, httponly=True, samesite='Lax', max_age=86400)
            return response, 200
        return jsonify({'error': 'Invalid credentials'}), 401
    except Exception as e:
        return jsonify({'error': str(e)}), 400

@auth_bp.route('/logout', methods=['POST'])
def logout():
    response = make_response(jsonify({'message': 'Logout successful'}))
    response.delete_cookie('token')
    return response, 200