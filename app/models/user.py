from sqlalchemy.dialects.postgresql import ARRAY
from . import db

class User(db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True)
    nama = db.Column(db.String(100))
    nip = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(100), unique=True)
    password_hash = db.Column(db.Text)
    roles = db.Column(ARRAY(db.String))  # contoh: ['kaprodi', 'dosen']
