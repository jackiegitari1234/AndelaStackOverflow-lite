import unittest
import json
from app import create_app

class TestAuthUsers(unittest.TestCase):
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()

        self.data1 = {
            "username":"jackie",
            "email":"jackie@gmail.com",
            "password":"FWfnghv",
            "confirm_pwrd":"FWfnghv"
        }
        self.data2 = {
            "username":"jackie",
            "email":"jackie@gmail.com"
        }
        self.data3 = {
            "username":"jackie",
            "email":"jackiegmail.com",
            "password":"FW3fnghv",
            "confirm_pwrd":"FW3fnghv"
        }
        self.data4 = {
            "username":"jackie",
            "email":"jackie@gmail.com",
            "password":"FW3fnghv",
            "confirm_pwrd":"FW3fnghv"
        }
        self.data5 = {
            "username":"muthoni",
            "email":"muthoni@gmail.com",
            "password":"FW3fnghv"
        }
        self.data6 ={
        "username" : "mee",
        "email" : "me@gmail.com",
        "password" : "Meeb1233"
        }
        self.data7 ={
        "username" : "mee",
        "email" : "me@gmail.com",
        "password" : "Mee123"
        }
        

    """ Test register with no input data"""
    def test_register_nodata(self):
        response = self.client.post('api/v1/register')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"POST of type Application/JSON expected")
        self.assertEqual(response.status_code, 400)

        """ Test register with empty fields"""
    def test_register_empty_fields(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data2),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"All fields are required")
        self.assertEqual(response.status_code, 400)


    """ Test register with invalid password"""
    def test_register_invalid_password(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a valid password")
        self.assertEqual(response.status_code, 400)

    """ Test register with invalid email"""
    def test_register_invalid_email(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a valid email")
        self.assertEqual(response.status_code, 400)

    """ Test valid registration"""
    def test_register_valid_input(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data4),content_type="application/json")
        self.assertEqual(response.status_code, 201) #201 created


    def test_login_nodata(self):
        response = self.client.post('api/v1/login')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"POST of type Application/JSON expected")
        self.assertEqual(response.status_code, 400)

        """ Test login with empty fields"""
    def test_login_empty_fields(self):
        response = self.client.post('api/v1/login',data=json.dumps(self.data2),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"All fields are required")
        self.assertEqual(response.status_code, 400)


    """ Test login with invalid password"""
    def test_login_invalid_password(self):
        response = self.client.post('api/v1/login',data=json.dumps(self.data1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a valid password")
        self.assertEqual(response.status_code, 400)

    """ Test regiloginster with invalid email"""
    def test_login_invalid_email(self):
        response = self.client.post('api/v1/login',data=json.dumps(self.data3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Please enter a valid email")
        self.assertEqual(response.status_code, 400)

    """ Test wrong email"""
    def test_login_wrong_email(self):
        response = self.client.post('api/v1/login',data=json.dumps(self.data5),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"User not Found")
        self.assertEqual(response.status_code, 404)

    """ Test wrong password"""
    def test_login_wrong_password(self):
        response = self.client.post('api/v1/login',data=json.dumps(self.data6),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Invalid Password")
        self.assertEqual(response.status_code, 400)

    def test_login_correct_details(self):
        response = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        self.assertEqual(response.status_code, 200)

   

    def tearDown(self):
        """ Destroy the test client when done """
        
        self.app.testing = False
        self.app = None

    
