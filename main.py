from flask import Flask, Blueprint, render_template
from blueprint.api import api_blueprint
from blueprint.pages.main import pages_blueprint

app = Flask(__name__)
app.register_blueprint(api_blueprint)
app.register_blueprint(pages_blueprint)

pages_blueprint = Blueprint("pages_blueprint", __name__)


if __name__ == "__main__":
    app.run(debug=True)
