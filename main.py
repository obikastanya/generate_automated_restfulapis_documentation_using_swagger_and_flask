from flask import Flask
from flask_restx import Api

from routes.cat import api as cat_namespace
from routes.login import api as login_namespace

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

api.add_namespace(cat_namespace, path='/cat')
api.add_namespace(login_namespace, path='/login')


app =Flask(__name__)
app.config["RESTX_MASK_SWAGGER"]=False
api.init_app(app)

if __name__=="__main__":
    app.run(debug=True, port=5000)