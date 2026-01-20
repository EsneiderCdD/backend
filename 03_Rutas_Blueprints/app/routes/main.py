from flask import Blueprint

bp = Blueprint('main', __name__)

@bp.route('/')
def status():
    return "Backend5 Running with Blueprints (Routes Layer)"
