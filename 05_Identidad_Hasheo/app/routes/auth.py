from flask import Blueprint, request, jsonify
from app.extensions import db
from app.models.usuario import Usuario

bp = Blueprint('auth', __name__, url_prefix='/api/auth')

@bp.route('/register', methods=['POST'])
def register():
    data = request.get_json()
    
    # 1. Crear Usuario (Sin validar, asumimos happy path)
    nuevo_usuario = Usuario(username=data['username'])
    
    # 2. Magia (Hasheo)
    nuevo_usuario.set_password(data['password']) 
    
    # 3. Guardar
    db.session.add(nuevo_usuario)
    db.session.commit()
    
    return jsonify(msg="Exito"), 201
