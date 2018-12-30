'''THIS IS THE GLUE'''

# from flask import Flask
from flask import Flask

create_app = Flask(__name__)
create_app.config['SECRET_KEY'] = "uudye78tgde6refs55w7iwtsj"

# local import
from app.api.v1.views.auth_view import v1 as Version1_auth
from app.api.v1.views.questions_view import v1 as Version1_questions

create_app.register_blueprint(Version1_auth)
create_app.register_blueprint(Version1_questions)
