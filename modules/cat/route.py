from flask import request
from flask_restx import Namespace, Resource

from utils.auth.auth import login_required

from .service import CatService
from .swagger.schema import CatSchema

ns = Namespace("Cats", "APIs related to cat modules")
ns.tags = ["cat"]
cat_service = CatService()
cat_schema = CatSchema(ns)


class CatResource(Resource):
    @ns.doc(security="apikey")
    @ns.doc(tags =["cat"])
    @login_required
    @ns.expect(cat_schema.find_cats_params())
    @ns.marshal_with(cat_schema.find_cats_response())
    def get(self):
        """Find cats"""
        args = request.args
        cat_name = None
        if args:
            cat_name = args.get("cat_name")

        return cat_service.find(cat_name)

    @ns.doc(security="apikey")
    @login_required
    @ns.expect(cat_schema.add_new_cat_payload())
    @ns.marshal_with(cat_schema.add_new_cat_response())
    def post(self):
        "Add a new cat"
        payload = request.json
        if not payload:
            return {"message": "Bad Request"}, 400
        cat_name = payload.get("cat_name")
        return cat_service.create(cat_name)


@ns.route("/<cat_id>/")
class CatDetailResource(Resource):
    @ns.doc(security="apikey")
    @login_required
    @ns.marshal_with(cat_schema.get_cat_response())
    def get(self, cat_id):
        "Get cat"
        return cat_service.get(cat_id)
