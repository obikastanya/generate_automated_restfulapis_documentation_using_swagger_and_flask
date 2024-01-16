from flask_restx import Namespace, Resource

ns = Namespace("Dogs", "APIs related to dog modules")


@ns.route('/dog')
class DogResource(Resource):
    def get(self):
        ...