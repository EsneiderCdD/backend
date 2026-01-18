from flask import Flask

# Importamos nuestro blueprint
from app.routes import main

def create_app():
    app = Flask(__name__)
    
    # 3. Registramos el Blueprint en la aplicación principal
    # Todo lo definido en main.bp se agrega a la app
    app.register_blueprint(main.bp)
    
    return app
