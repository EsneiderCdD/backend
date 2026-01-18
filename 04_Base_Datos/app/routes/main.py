from flask import Blueprint
from app.extensions import db
from sqlalchemy import text  # Para hacer una consulta SQL cruda de prueba

bp = Blueprint('main', __name__)

@bp.route('/')
def status():
    # Pequeña prueba para ver si la DB responde
    try:
        db.session.execute(text('SELECT 1'))
        db_status = "Conectada"
    except Exception as e:
        db_status = f"Error: {str(e)}"
        
    return f"Backend6 Running (PostgreSQL Status: {db_status})"
