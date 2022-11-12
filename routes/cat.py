from flask_restx import Namespace, Resource
from models.cat import CatModel

# add
from flask import request

api = Namespace('Cats',"APIs related to cat modules")
cat_model=CatModel(api)

cat_dummy_data=[
            {'id': '1', 'name': 'Whiskers'},
            {'id': '2', 'name': 'Fluffy'},
            {'id': '3', 'name': 'Shawn'}
]

@api.route('/')
class CatResource(Resource):
 
    @api.expect(cat_model.get_cats_expected_params())
    @api.marshal_with(cat_model.get_cats())
    def get(self):
        "List all cats"
        filter_cat_name=request.args.get("cat_name", "")
        
        if not filter_cat_name:
            return {"data":cat_dummy_data, "message":"OK"}, 200
        
        cats=[]
        for cat in cat_dummy_data :
            if cat.get("name").lower() == filter_cat_name.lower():
                cats.append(cat)
        
        if cats:
            return {"data":cats, "message":"OK"}, 200
        
        return {"data":cats, "message":"Cats is not found"}, 404

    @api.expect(cat_model.add_new_cat_expected_payload())
    @api.marshal_with(cat_model.add_new_cat())
    def post(self):
        "Add Cat"
        new_cat={
            "id":int(cat_dummy_data[-1].get('id')) +1,
            "name":request.json.get("cat_name")
        }
        cat_dummy_data.append(new_cat)

        return {"data":new_cat, "message":"OK"}, 200


@api.route('/<cat_id>')
class CatList(Resource):

    @api.marshal_with(cat_model.get_cat())
    def get(self, cat_id):
        "Get cat"
        for cat in cat_dummy_data:
            if cat.get("id") == cat_id:
                return {"data":cat, "message":"OK"}, 200

        return {"data":{}, "message":"Cat is not found"}, 404
