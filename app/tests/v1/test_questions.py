import unittest
import json
from app import create_app
from app.api.v1.utils.validator import token_check

class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()

        self.question1 ={
        "id" : 1,
        "owner_email" : "james@gmail.com",
        "question" : "what is java?"
        }
        
    def test_unloggedin_user(self):
        response = self.client.post('api/v1/questions')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"Token is missing")
        self.assertEqual(response.status_code, 401)

    def test_all_questions(self):
        response = self.client.get('api/v1/questions')
        self.assertEqual(response.status_code, 200)

    def test_specific_question(self): #no answers
        response = self.client.get('api/v1/questions/3')
        result = json.loads(response.data)
        self.assertEqual(result["answers"],"no answers yet")
        self.assertEqual(response.status_code, 200)

    def test_invalid_id(self): 
        response = self.client.get('api/v1/questions/7')
        result = json.loads(response.data)
        self.assertEqual(result["message"],"No question with id 7 found")
        self.assertEqual(response.status_code, 400)

    

    

  