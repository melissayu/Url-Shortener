from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

shortenerapp = Flask(__name__)
shortenerapp.config.from_object('config')
db = SQLAlchemy(shortenerapp)

from shortenerapp import views, models

