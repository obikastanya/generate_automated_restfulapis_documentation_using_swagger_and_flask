from flask import Flask
from flask_restx import Api

from routes.cat import api as cat_namespace

api = Api(
    title="Pets Shop API",
    version="1.0",
    description="API for Pets Shop App",
    doc="/doc"
)

api.add_namespace(cat_namespace, path='/cat')


app =Flask(__name__)
app.config["RESTX_MASK_SWAGGER"]=False
api.init_app(app)

if __name__=="__main__":
    app.run(debug=True, port=5000)