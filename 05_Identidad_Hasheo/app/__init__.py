from flask import Flask
from app.config.config import Config
from app.extensions import db, migrate
from app.routes import auth
from app.models.usuario import Usuario  # Fix para que Migrate detecte el modelo

def create_app():
    app = Flask(__name__)
    
    app.config.from_object(Config)
    
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 3. Registrar Blueprints
    app.register_blueprint(auth.bp)
    
    return app
