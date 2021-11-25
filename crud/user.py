import json

from typing import Any, Dict, List


class UserCRUD:
    def __init__(self, filename: str) -> None:
        self.filename = filename

        self.read_from_file()

    def read_from_file(self) -> None:
        with open(self.filename, "r") as file:
            self.data = json.load(file)

    def write_to_file(self) -> None:
        with open(self.filename, "w") as file:
            json.dump(self.data, file)

    def add_new(self, login: str, data: Dict[str, Any]) -> None:
        if login in self.data:
            raise ValueError(f"User with login {login} already exists")

        self.set_item(login, data)

    def set_item(self, login: str, data: Dict[str, Any]) -> None:
        self.data[login] = data

    def get_item(self, login):
        if login not in self.data:
            return None

        return self.data[login]

        # return self.data.get(login)

    def delete_item(self, login: str) -> None:
        del self.data[login]

    def get_all_users(self) -> List[str]:
        return list(self.data)
