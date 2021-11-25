from flask import jsonify, request, Blueprint
from crud import UserCRUD
from pydantic import BaseModel, Field

user_blueprint = Blueprint("user_api", __name__)

user = UserCRUD("users.json")


@user_blueprint.route("/user")
def get_all_users():
    return jsonify(user.get_all_users())


class NewUserModel(BaseModel):
    login: str
    password: str = Field(min_length=8)


@user_blueprint.route("/user", methods=["POST"])
def create_new_user():
    """Register a new user."""

    new_user = NewUserModel(**request.json)  # type: ignore

    if user.get_item(new_user.login) is not None:
        return jsonify({"info": "User with such name already exists"}), 403

    user.set_item(new_user.login, {"password": new_user.password})
    user.write_to_file()

    return jsonify({"info": "Success"})

