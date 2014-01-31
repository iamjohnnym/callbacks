from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.restful import Api


app = Flask(__name__)
api = Api(app)
app.debug = True
app.config.from_object('config')
db = SQLAlchemy(app)

from app import views, models, api_views
