from functools import wraps

import jwt
from flask import request

from config import AppConfig


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        token = request.headers.get("token")
        if not token:
            return {"message": "Forbidden access"}

        try:
            jwt.decode(token, AppConfig.JWT_SECRET_KEY, algorithms="HS256")
        except jwt.ExpiredSignatureError:
            return {"message": "Forbidden access"}
        except:
            return {"message": "Invalid Token"}

        return func(*args, **kwargs)

    return wrapper
