from flask_restx import Namespace, Resource
from models.cat import CatModel

api = Namespace('Cats',"APIs related to cat modules")
cat_model=CatModel(api)

cat_dummy_data=[
            {'id': '1', 'name': 'Whiskers'},
            {'id': '2', 'name': 'Fluffy'},
            {'id': '3', 'name': 'Shawn'}
]

@api.route('/')
class CatResource(Resource):

    @api.marshal_with(cat_model.get_cats())
    def get(self):
        "List all cats"
        return {"data":cat_dummy_data, "message":"Cats is not found"}, 200
