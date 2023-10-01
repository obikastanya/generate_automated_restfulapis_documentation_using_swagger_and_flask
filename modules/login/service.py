import jwt

from config import AppConfig
from .model import LoginModel


class LoginService:
    def __init__(self):
        self.login_model = LoginModel()

    def login(self, username: str, password: str) -> dict:
        """Login"""

        default_user = self.login_model.get_default_user()

        is_identical_username = default_user.get("username") == username
        is_identical_password = default_user.get("password") == password

        token = None
        if is_identical_username and is_identical_password:
            token = jwt.encode(
                {"username": default_user.get("username")},
                AppConfig.JWT_SECRET_KEY,
                algorithm="HS256",
            )

        if token:
            return {"data": {"token": token}, "message": "OK"}, 200

        return {
            "data": {"token": token},
            "message": "Incorrect username or password",
        }, 500
