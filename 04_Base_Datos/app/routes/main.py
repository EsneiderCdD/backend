from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def status():
    return "04_Base_Datos Running"
