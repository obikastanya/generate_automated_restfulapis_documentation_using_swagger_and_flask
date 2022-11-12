from flask_restx import fields
from flask_restx import reqparse

class CatModel:
    def __init__(self, namespace):
        self.namespace=namespace
    
    def get_cats(self):
        data_model={
            "data":fields.List(
                fields.Nested(self._a_cat())
            ),
            "message":fields.String()
        }
        return self.namespace.model('get_cats_model',data_model )

    def _a_cat(self):
        data_model={
            "id":fields.String(),
            "name":fields.String()
        }
        return self.namespace.model('a_cat_model',data_model )
    
    def get_cats_expected_params(self):
        parser=reqparse.RequestParser()
        parser.add_argument("cat_name", type=str, help="Optional filter by cat names", location="args" )
        return parser
    
    def add_new_cat_expected_payload(self):
        data_model={
            "cat_name":fields.String(required=True, description="The cat name")
        }
        return self.namespace.model('add_cat_expected_payload',data_model )
    
    def add_new_cat(self):
        data_model={
            "data":fields.Nested(self._a_cat()),
            "message":fields.String()
        }
        return self.namespace.model('add_new_cat',data_model )
    
    def get_cat(self):
        data_model={
            "data":fields.Nested(self._a_cat()),
            "message":fields.String()
        }
        return self.namespace.model('get_cat',data_model )
