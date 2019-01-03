import re
from werkzeug.security import generate_password_hash, check_password_hash
from functools import wraps
from flask import jsonify, request
from app import create_app
import datetime
from flask_jwt import jwt


# compare password stored and user input
def compare_password(hash_pwrd, password):
    return check_password_hash(hash_pwrd,password)

#encrypt password
def encrypt_password(password):
    password_hash = generate_password_hash(password)
    return password_hash

#confirm password input
def confirm_password(password, confirmpwrd):
    if password == confirmpwrd:
        return True

class validate_inputs():

    def validate_email(self, email):
        return re.match(r"(^[a-zA-z0-9_.]+@[a-zA-z0-9-]+\.[a-z]+$)", email)

    def validate_password(self, password):

        if len(password) < 6:
            return False

        total = {}

        for letter in password:
            if letter.islower():
                total['has_lower'] = 1

            if letter.isupper():
                total['has_upper'] = 1

            if letter.isdigit():
                total['has_digit'] = 1

        return sum(total.values()) == 3

def token_check(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        if "x-access-token" in request.headers:
            token = request.headers['x-access-token']

        if not token:
            return jsonify({"message": "Token is missing"}), 401

        try:
            data = jwt.decode(token, create_app.config["SECRET_KEY"], options={"verify_iat": False},algorithms="HS256")
            current_user = data["email"]

        except: 
            return jsonify({"message" : "Token is invalid or expired"}), 401

        return f(current_user, *args, **kwargs)
    return decorated

