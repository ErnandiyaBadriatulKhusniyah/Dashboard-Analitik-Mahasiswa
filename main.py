# main.py
from flask import Flask
from flask_cors import CORS
from app.models import db
from app.routes.mahasiswa import mahasiswa_bp
from app.routes.auth import auth_bp
from app.routes.matakuliah import matakuliah_bp
from app.api.rekomendasi_transkrip import bp as api_bp
from flask_migrate import Migrate
from dotenv import load_dotenv
import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'your_secret_key'
    load_dotenv()
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'postgresql://postgres:root@localhost/DashboardAnalitik'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    Migrate(app, db)  
    CORS(app)

    # Register Blueprints
    app.register_blueprint(mahasiswa_bp)
    app.register_blueprint(auth_bp)
    app.register_blueprint(matakuliah_bp)
    app.register_blueprint(api_bp)


    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
