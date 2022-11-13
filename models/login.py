from flask_restx import fields

class LoginModel:
    def __init__(self, namespace):
        self.namespace=namespace
    
    def login_expected_payload(self):
        data_model={
            "username":fields.String(),
            "password":fields.String(),
        }
        return self.namespace.model("login_expected_payload", data_model)

    def login(self):
        data_model={
            "data":fields.Nested(self._token()),
            "message":fields.String()
        }
        return self.namespace.model("login", data_model)
    
    def _token(self):
        data_model={
            "token":fields.String()
        }
        return self.namespace.model("token", data_model)