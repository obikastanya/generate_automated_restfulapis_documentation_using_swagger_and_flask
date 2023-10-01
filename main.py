from flask import Flask
from flask_restx import Api

from config import AppConfig

from modules.cat.route import ns as cat_namespace
from modules.login.route import ns as login_namespace


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
api.add_namespace(cat_namespace, path='/cat')


app =Flask(__name__)
app.config.from_object(AppConfig)
api.init_app(app)

if __name__=="__main__":
    app.run(debug=True, port=5000)