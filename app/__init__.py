'''THIS IS THE GLUE'''

from flask import Flask

#local import
from app.api.v1.views.auth_view import v1 as Version1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(Version1)
    return app