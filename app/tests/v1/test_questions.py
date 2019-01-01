import unittest
import json
from app import create_app
from app.api.v1.utils.validator import token_check

class TestQuestions(unittest.TestCase):
    def setUp(self):
        self.app = create_app
        self.client = self.app.test_client()

        self.data7 ={
        "username" : "mee",
        "email" : "me@gmail.com",
        "password" : "Mee123"
        }
        self.data8 ={
        "username" : "james",
        "email" : "james@gmail.com",
        "password" : "James123"
        }

        self.question1 ={
        "id" : 1,
        "owner_email" : "james@gmail.com",
        "question" : "what is java?"
        }
        self.question2 ={
        "id" : 2,
        "owner_email" : "james@gmail.com",
        }
        
        self.answer1 = {
            "id" : 3
        }

        self.answer2 = {
            "answer" : "a programming language that develops APIs"
        }

    def test_app_is_development(self):
        self.assertTrue(create_app.config['DEBUG'] is True)
        self.assertFalse(create_app is None)
        
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

    def test_post_question(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        response = self.client.post('api/v1/questions',headers={"x-access-token":res},data=json.dumps(self.question1),content_type="application/json")
        self.assertEqual(response.status_code, 201)

    def test_post_question_empty_field(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        newresponse = self.client.post('api/v1/questions',headers={"x-access-token":res},data=json.dumps(self.question2),content_type="application/json")
        result = json.loads(newresponse.data)
        self.assertEqual(result["message"], "Please type-in a question")
        self.assertEqual(newresponse.status_code, 400)

    def test_diplay_question_and_answers(self):
        response = self.client.get('api/v1/questions/3',data=json.dumps(self.question1),content_type="application/json")
        result = json.loads(response.data)
        self.assertEqual(result["answers"],"no answers yet")
        self.assertEqual(response.status_code, 200)

    def test_post_answer_empty_value(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        answer_response = self.client.post('api/v1/questions/1/answer',headers={"x-access-token":res},data=json.dumps(self.answer1),content_type="application/json")
        answer_result = json.loads(answer_response.data)
        self.assertEqual(answer_result["message"], "Please type-in an answer")
        self.assertEqual(answer_response.status_code, 400)

    def test_post_answer(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        answer_response = self.client.post('api/v1/questions/2/answer',headers={"x-access-token":res},data=json.dumps(self.answer2),content_type="application/json")
        answer_result = json.loads(answer_response.data)
        self.assertEqual(answer_result ["message"], "answer posted successfullY")
        self.assertEqual(answer_response.status_code, 200)

    def test_delete_question_unauthorised(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        answer_response = self.client.delete('api/v1/questions/1',headers={"x-access-token":res},data=json.dumps(self.answer2),content_type="application/json")
        answer_result = json.loads(answer_response.data)
        self.assertEqual(answer_result ["message"], "previlige denied")
        self.assertEqual(answer_response.status_code, 200)

    def test_delete_inexistince_question(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data7),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        answer_response = self.client.delete('api/v1/questions/9',headers={"x-access-token":res},data=json.dumps(self.answer2),content_type="application/json")
        answer_result = json.loads(answer_response.data)
        self.assertEqual(answer_result ["message"], "No question with id 9 found")
        self.assertEqual(answer_response.status_code, 400)

    def test_delete_valid_question(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data8),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        answer_response = self.client.delete('api/v1/questions/1',headers={"x-access-token":res},data=json.dumps(self.answer2),content_type="application/json")
        answer_result = json.loads(answer_response.data)
        self.assertEqual(answer_result ["message"], "deleted successfully")
        self.assertEqual(answer_response.status_code, 200)

    def test_update_answer_unauthorised_user(self):
        resp_login = self.client.post('api/v1/login',data=json.dumps(self.data8),content_type="application/json")
        login_result = json.loads(resp_login.data)
        res = login_result["token"]
        answer_response = self.client.put('api/v1/questions/2/answers/3',headers={"x-access-token":res})
        answer_result = json.loads(answer_response.data)
        self.assertEqual(answer_result ["message"], "user not authorised")


    
       

    

    

  