from flask import request
from flask_restx import Namespace, Resource
from models.login import LoginModel
import jwt


api = Namespace('Login',"APIs related to Login Auth")
login_model=LoginModel(api)

default_user={
    "username":"admin",
    "password":"admin"
}

jwt_secret_key="this is screet key to generate jwt token"


@api.route('/')
class Credential(Resource):

    @api.expect(login_model.login_expected_payload())
    @api.marshal_with(login_model.login())
    def post(self):
        "Login"
        is_identical_username= default_user.get('username') == request.json.get("username")
        is_identical_password= default_user.get('password') == request.json.get("password")

        token=None
        if is_identical_username and is_identical_password:
            token=jwt.encode(
                {"username":default_user.get('username')},
                jwt_secret_key,
                algorithm="HS256"
            )
        
        if token:
            return {"data":{"token":token}, "message":"OK"}, 200

        return {"data":{"token":token}, "message":"Incorrect username or password"}, 500
        
