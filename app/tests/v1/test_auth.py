import unittest
import json
from app.tests.v1.base_test import BaseTest

class TestAuthUsers(BaseTest):
    def setUp(self):

        self.data1 = {
            "username":"jackie",
            "email":"jackie@gmail.com",
            "password":"FWfnghv"
        }
        self.data2 = {
            "username":"jackie",
            "email":"jackie@gmail.com"
        }
        self.data3 = {
            "username":"jackie",
            "email":"jackiegmail.com",
            "password":"FW3fnghv"
        }
        self.data4 = {
            "username":"jackie",
            "email":"jackie@gmail.com",
            "password":"FW3fnghv"
        }
        super().setUp()

    """ Test register with no input data"""
    def test_register_nodata(self):
        response = self.client.post('api/v1/register')
        result = json.loads(response.data)
        self.assertEqual(result["alert"],"Please fill in user information")
        self.assertEqual(response.status_code, 400)

        """ Test register with empty fields"""
    def test_register_empty_fields(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data2),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["alert"],"All fields are required")
        self.assertEqual(response.status_code, 400)


    """ Test register with invalid password"""
    def test_register_invalid_password(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["alert"],"Please enter a valid password")
        self.assertEqual(response.status_code, 400)

    """ Test register with invalid email"""
    def test_register_invalid_email(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data3),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["alert"],"Please enter a valid email")
        self.assertEqual(response.status_code, 400)

    """ Test valid registration"""
    def test_register_valid_input(self):
        response = self.client.post('api/v1/register',data=json.dumps(self.data4),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Registration successful")
        self.assertEqual(response.status_code, 201)


    

if __name__ == "__main__":
    unittest.main()