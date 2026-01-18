from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .extensions import db, migrate, jwt
import os

from app.routes.auth import auth as auth_bp
from app.models.usuario import Usuario



load_dotenv()

def create_app():
    app = Flask(__name__)
    CORS(app)

    env = os.getenv("FLASK_ENV", "development").capitalize() + "Config"
    app.config.from_object(f"app.config.config.{env}")

    
            
    app.register_blueprint(auth_bp)
    
    db.init_app(app)
    migrate.init_app(app, db)
    jwt.init_app(app)

    @app.route("/")
    def index():
        return "Hello World"

    return app
