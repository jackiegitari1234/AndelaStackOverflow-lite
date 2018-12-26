'''REGISTER ENDPOINT'''

from flask import jsonify, Blueprint,request
from app.api.v1.utils.validator import validate_inputs
from .. import version1 as v1

validate_inputs = validate_inputs()

@v1.route('/register', methods=['POST'])
def reg_validation():

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "alert": "Please fill in user information"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["username", "email", "password"]):
        return jsonify({"status": 400, "alert": "All fields are required"}), 400 

    
    email = data['email']
    password = data['password']

    # Email validation
    if not validate_inputs.validate_email(email):
        return jsonify({"status": 400, "alert": "Please enter a valid email"}), 400

    #password validation
    if not validate_inputs.validate_password(password):
        return jsonify({"status": 400, "alert": "Please enter a valid password"}), 400

    return jsonify({"status": 201, "message": "Registration successful"}), 201

