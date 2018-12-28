'''THIS IS THE GLUE'''

from flask import Flask

#local import
from app.api.v1.views.auth_view import v1 as Version1
from app.api.v1.views.questions_view import v1 as Vers1


def create_app():
    app = Flask(__name__)
    app.register_blueprint(Version1)
    app.register_blueprint(Vers1)
    return app