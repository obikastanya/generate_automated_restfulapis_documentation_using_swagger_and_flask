from flask_restx import fields

from utils.swagger.base_schema import Schema
from utils.swagger.common_data_sample import Response
from .data_sample import User, Token

user_data_sample = User()
token_data_sample = Token()
response_data_sample = Response()


class LoginSchema(Schema):
    def __init__(self, namespace):
        self.namespace = namespace
        self.name = "Login"

    def login_payload(self):
        data_model = {
            "username": fields.String(example=user_data_sample.username),
            "password": fields.String(example=user_data_sample.password),
        }
        schema_name = self.create_name("login_payload")
        return self.namespace.model(schema_name, data_model)

    def login_response(self):
        data_model = {
            "data": fields.Nested(self._token()),
            "message": fields.String(example=response_data_sample.http_responses[200]),
        }
        schema_name = self.create_name("login_response")
        return self.namespace.model(schema_name, data_model)

    def _token(self):
        data_model = {"token": fields.String(example=token_data_sample.token)}
        schema_name = self.create_name("_token")
        return self.namespace.model(schema_name, data_model)
