from functools import wraps
from flask import request, jsonify, current_app
from models import User
import jwt

def token_required(f):
    @wraps(f)
    def decorated(*args, **kwargs): 
        token = request.cookies.get('token')
        if not token:
            return jsonify({'message': 'Token is missing!'}), 401
        try:
            secret = current_app.config.get('SECRET_KEY', 'your_secret_key')
            data = jwt.decode(token, secret, algorithms=["HS256"])
            current_user = User.query.filter_by(user_id=data['user_id']).first()
        except Exception:
            return jsonify({'message': 'Token is invalid!'}), 401
        return f(current_user, *args, **kwargs)
    return decorated
