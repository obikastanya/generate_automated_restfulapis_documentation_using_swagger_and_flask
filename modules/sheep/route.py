from flask_restx import Namespace, Resource

ns = Namespace("Sheeps", "APIs related to sheep modules")


@ns.route('/sheep')
class SheepResource(Resource):
    def get(self):
        ...