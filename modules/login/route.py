from flask import request
from flask_restx import Namespace, Resource

from .service import LoginService

from .swagger.schema import LoginSchema


ns = Namespace("Login", "APIs related to Login Auth")
ns.tags = ["cat"]

login_service = LoginService()
login_schema = LoginSchema(ns)


@ns.route("/")
class LoginResource(Resource):
    @ns.doc(tags =["cat"])
    @ns.expect(login_schema.login_payload())
    @ns.marshal_with(login_schema.login_response())
    def post(self):
        """Login"""
        payload = request.json
        if payload is None:
            return {"message": "Bad Request"}, 400

        username = payload.get("username")
        password = payload.get("password")

        return login_service.login(username, password)
