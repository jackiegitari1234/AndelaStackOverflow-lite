'''THIS IS THE GLUE'''
from flask import Flask

APP = Flask(__name__)

from app.api.v1.views.auth_view import v1 as Version1
APP.register_blueprint(Version1)