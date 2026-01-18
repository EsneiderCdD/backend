from flask import Blueprint, request
from app.extensions import db
from app.models.usuario import Usuario
from flask_jwt_extended import create_access_token
from datetime import timedelta

auth = Blueprint("auth", __name__, url_prefix="/auth")


@auth.route("/register", methods=["POST"])
def register():
    data = request.get_json()

    name = data.get("name")
    password = data.get("password")

    if not name or not password:
        return {"message": "Missing username or password"}, 400

    if Usuario.query.filter_by(name=name).first():
        return {"message": "User already exists"}, 400

    nuevo_usuario = Usuario(name=name)
    nuevo_usuario.set_password(password)

    db.session.add(nuevo_usuario)
    db.session.commit()

    return {"message": "User registered successfully"}, 201


@auth.route("/login", methods=["POST"])
def login():
    data = request.get_json()

    name = data.get("name")
    password = data.get("password")

    if not name or not password:
        return {"message": "Missing username or password"}, 400

    usuario = Usuario.query.filter_by(name=name).first()

    if not usuario or not usuario.check_password(password):
        return {"message": "Invalid username or password"}, 401

    token = create_access_token(
        identity=usuario.id,
        expires_delta=timedelta(days=1)
    )

    return {
        "access_token": token,
        "user": {
            "id": usuario.id,
            "name": usuario.name,
            "role": usuario.role
        }
    }, 200
