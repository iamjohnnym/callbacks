from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
#from flask.ext.restful import Api
from flask.ext.restless import APIManager
from flask.ext.login import LoginManager


app = Flask(__name__)
app.debug = True
app.config.from_object('config')
lm = LoginManager()
lm.init_app(app)
db = SQLAlchemy(app)
api = APIManager(app, flask_sqlalchemy_db=db)

from app import views, models
callbacks_blueprint = api.create_api(models.Callbacks,
    methods=['DELETE', 'GET', 'POST', 'PUT'], max_results_per_page=-1)
callback_data_blueprint = api.create_api(models.CallbackDetails, methods=['DELETE', 'GET', 'PUT', 'POST'])
callback_data_blueprint = api.create_api(models.ActiveTickets, methods=['DELETE','GET', 'PUT', 'POST'])
callback_data_blueprint = api.create_api(models.User, methods=['DELETE','GET', 'PUT', 'POST'])
