from flask_restx import fields
from flask_restx import reqparse

from utils.swagger.base_schema import Schema
from utils.swagger.common_data_sample import Response

from .data_sample import Cat

cat_data_sample = Cat()
response_data_sample = Response()


class CatSchema(Schema):
    def __init__(self, namespace):
        self.namespace = namespace
        self.name = "Cat"

    def find_cats_params(self):
        parser = reqparse.RequestParser()
        parser.add_argument(
            "cat_name",
            type=str,
            help=f"Optional filter by cat names (e.g., {cat_data_sample.name})",
            location="args",
        )
        return parser

    def find_cats_response(self):
        data_model = {
            "data": fields.List(fields.Nested(self._a_cat())),
            "message": fields.String(example=response_data_sample.http_responses[200]),
        }
        schema_name = self.create_name("find_cats")
        return self.namespace.model(schema_name, data_model)

    def add_new_cat_response(self):
        data_model = {
            "data": fields.Nested(self._a_cat()),
            "message": fields.String(response_data_sample.http_responses[201]),
        }
        return self.namespace.model(f"{self.name}_add_new_cat", data_model)

    def get_cat_response(self):
        data_model = {
            "data": fields.Nested(self._a_cat()),
            "message": fields.String(response_data_sample.http_responses[200]),
        }
        return self.namespace.model(f"{self.name}_get_cat", data_model)

    def add_new_cat_payload(self):
        data_model = {
            "cat_name": fields.String(required=True, default=cat_data_sample.name),
            "colors": fields.List(
                fields.Nested(self._cat_color()), example=cat_data_sample.colors
            ),
        }
        schema_name = self.create_name("add_new_cat_payload")
        return self.namespace.model(schema_name, data_model)

    def _a_cat(self):
        data_model = {
            "id": fields.String(example=cat_data_sample.id),
            "name": fields.String(example=cat_data_sample.name),
        }
        schema_name = self.create_name("_a_cat")
        return self.namespace.model(schema_name, data_model)

    def _cat_color(self):
        data_model = {"color": fields.String()}
        schema_name = self.create_name("_cat_color")
        return self.namespace.model(schema_name, data_model)
