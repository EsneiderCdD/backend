from flask import Blueprint

# 1. Creamos el "Plano" (Blueprint)
# 'main' es el nombre interno del blueprint
# __name__ ayuda a Flask a localizar recursos si los hubiera
bp = Blueprint('main', __name__)

# 2. Definimos las rutas asociadas a este plano
@bp.route('/')
def status():
    return "Backend5 Running with Blueprints (Routes Layer)"
