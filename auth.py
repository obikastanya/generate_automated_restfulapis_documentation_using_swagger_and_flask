import jwt
from flask import request
from functools import wraps

jwt_secret_key="this is screet key to generate jwt token"

def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        token=request.headers.get("token")
        if not token:
            return {"message":'Forbidden access'}

        try:
            jwt.decode(token, jwt_secret_key, algorithms='HS256')
        except jwt.ExpiredSignatureError:
            return {"message":'Forbidden access'}
        except:
            return {"message":'Invalid Token'}

        return func(*args, **kwargs)
    return wrapper
