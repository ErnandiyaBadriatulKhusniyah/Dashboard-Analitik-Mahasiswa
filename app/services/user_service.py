from models import User
import bcrypt

def is_email_or_nip_registered(email, nip):
    return User.query.filter((User.email == email) | (User.nip == nip)).first()

def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

def verify_password(plain: str, hashed: str) -> bool:
    return bcrypt.checkpw(plain.encode('utf-8'), hashed.encode('utf-8'))
