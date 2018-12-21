""" app_api """
from flask import Flask


def create_app():
    app = Flask(__name__)
    # app.register_blueprint(v1)
    return app