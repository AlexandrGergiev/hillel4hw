from flask import Blueprint
from .user import user_blueprint

api_blueprint = Blueprint("api_blueprint", __name__, url_prefix="/api")
api_blueprint.register_blueprint(user_blueprint)
