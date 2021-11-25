from flask import Blueprint, render_template

pages_blueprint = Blueprint("pages_blueprint", __name__)


@pages_blueprint.route("/")
def index():
    return render_template("register.html")

