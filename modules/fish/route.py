from flask_restx import Namespace, Resource

ns = Namespace("Fish", "APIs related to fish modules")


@ns.route('/fish')
class FishResource(Resource):
    def get(self):
        ...