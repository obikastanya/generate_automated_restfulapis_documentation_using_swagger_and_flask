class LoginModel:
    def __init__(self):
        self._default_user = {"username": "admin", "password": "admin"}

    def get_default_user(self):
        return self._default_user
