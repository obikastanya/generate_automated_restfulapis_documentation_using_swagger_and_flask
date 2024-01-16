from flask import Flask
from api import Api

from config import AppConfig

from modules.login.route import ns as login_namespace
from modules.fish.route import ns as fish_namespace
from modules.cat.route import ns as cat_namespace
from modules.sheep.route import ns as sheep_namespace
from modules.dog.route import ns as dog_namespace


api = Api(
    title="Pets Shop API",
    version="1.0",
    description="API for Pets Shop App",
    doc="/doc",
    authorizations={
        "apikey":{
            "type":"apiKey",
            "in":"header",
            "name":"token"
        }
    }
    
)

api.add_namespace(login_namespace, path='/login')
api.add_namespace(dog_namespace, path='/dog')
api.add_namespace(fish_namespace, path='/fish')
api.add_namespace(cat_namespace, path='/cat')
api.add_namespace(sheep_namespace, path='/sheep')


app =Flask(__name__)
app.config.from_object(AppConfig)
api.init_app(app)

if __name__=="__main__":
    app.run(debug=True, port=5000)