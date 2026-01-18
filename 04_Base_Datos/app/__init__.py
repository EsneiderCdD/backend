from flask import Flask
from app.config.config import Config
from app.extensions import db, migrate
from app.routes import main

def create_app():
    app = Flask(__name__)
    
    # 1. Cargar Configuración (incluyendo DATABASE_URL)
    app.config.from_object(Config)
    
    # 2. Inicializar Extensiones con la app
    db.init_app(app)
    migrate.init_app(app, db)
    
    # 3. Registrar Blueprints
    app.register_blueprint(main.bp)
    
    return app
