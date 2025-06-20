from flask import Blueprint, request, jsonify, make_response, current_app
from models import db, User
from auth.token import token_required
import bcrypt
import jwt
from datetime import datetime, timedelta

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/register', methods=['POST'])
def register():
    try:
        data = request.json
        roles = data['roles']

        if 'kaprodi' in roles:
            existing_kaprodi = User.query.filter(User.roles.any('kaprodi')).first()
            if existing_kaprodi:
                return jsonify({'error': 'Role kaprodi sudah terpakai'}), 400
        else:
            if len(roles) > 1 or roles[0] != 'dosen':
                return jsonify({'error': 'Role dosen hanya boleh satu dan tidak bisa merangkap'}), 400

        if User.query.filter_by(email=data['email']).first():
            return jsonify({'error': 'Email already registered'}), 400
        if User.query.filter_by(nip=data['nip']).first():
            return jsonify({'error': 'NIP already registered'}), 400

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
                    'peran': user.roles
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
