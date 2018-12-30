'''REGISTER ENDPOINT'''

from flask import jsonify, Blueprint,request,abort,make_response
from app.api.v1.utils.validator import encrypt_password,compare_password,confirm_password,validate_inputs
from app.api.v1 import version1 as v1
from app.api.v1.models.users_model import User,users
from app import create_app
import datetime
from flask_jwt import jwt

validate_inputs = validate_inputs()

@v1.route('/register', methods=['POST'])
def reg_validation():

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["username", "email", "password", "confirm_pwrd"]):
        return jsonify({"status": 400, "message": "All fields are required"}), 400 

    username = data['username']
    email = data['email']
    password = data['password']
    confirm_pwrd = data['confirm_pwrd']

    # Email validation
    if not validate_inputs.validate_email(email):
        return jsonify({"status": 400, "message": "Please enter a valid email"}), 400

    #password validation
    if not validate_inputs.validate_password(password):
        return jsonify({"status": 400, "message": "Please enter a valid password"}), 400

    #confirm password
    if not confirm_password(password, confirm_pwrd):
        return jsonify({"status": 400, "message": "Please enter a matching password"}), 400

    find_usr = User().find_user(email)
    if find_usr:
        return jsonify({"status": 400, "message": "user alrealdy exists, please use a different email"}), 400

    
    hash_pwd = encrypt_password(password) #encrypt password
    user = User(email,username,hash_pwd).add_user() #append user
    return jsonify(user), 201


@v1.route('/login', methods=['POST'])
def login_validation():

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["email", "password"]):
        return jsonify({"status": 400, "message": "All fields are required"}), 400 

    
    email = data['email']
    password = data['password']

    # Email validation
    if not validate_inputs.validate_email(email):
        return jsonify({"status": 400, "message": "Please enter a valid email"}), 400

    #password validation
    if not validate_inputs.validate_password(password):
        return jsonify({"status": 400, "message": "Please enter a valid password"}), 400

    #check if email exists
    find_usr = User().find_user(email)
    if not find_usr:
        abort(make_response(jsonify({"message":"User not Found"}),404))

    #Check if password match
    if not compare_password(find_usr['password'],password):
        abort(make_response(jsonify({'message':'Invalid Password'}),400))

    

    token = jwt.encode({"email": email, 'exp' : datetime.datetime.utcnow()+ datetime.timedelta(minutes=30)}, create_app.config["SECRET_KEY"])
    return jsonify({"token": token.decode('UTF-8')}), 200
       
    
        
