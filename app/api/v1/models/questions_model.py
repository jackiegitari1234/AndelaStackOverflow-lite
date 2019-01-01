questions = [
    {
        "id" : 1,
        "owner_email" : "james@gmail.com",
        "question" : "what is java?"
    },
    {
        "id" : 2, 
        "owner_email" : "jackie@gmail.com",
        "question" : "what is a compiler?",
    },
    {
        "id" : 3, 
        "owner_email" : "mike@gmail.com",
        "question" : "what is a TDD?",
    }
]
answers = [
    {
        "id" : 1,
        "question_id" : 1,
        "member_email" : "lucy@gmail.com",
        "answer" : "A programming language"
    },
    {
        "id" : 2, 
        "question_id" : 1,
        "member_email" : "jackie@gmail.com",
        "answer" : "A server side programming language"
    },
     {
        "id" : 3, 
        "question_id" : 2,
        "member_email" : "lucy@gmail.com",
        "answer" : "A server side programming language"
    }
]
class quiz(object):    
    
    def __init__(self, question=None, current_user=None):
        self.quiz_id = len(questions)+1
        self.question = question
        self.current_user = current_user

    def add_quiz(self):
        quiz = {
            "id": self.quiz_id,
            "question": self.question,
            "owner_email":self.current_user
        }
        questions.append(quiz)
        return questions

class answer(object):    
    
    def __init__(self, answer=None,question_id=None,current_user=None):
        self.answr_id = len(questions)+1
        self.question_id = question_id
        self.answer = answer
        self.current_user = current_user

    def add_answer(self):
        ansr = {
            "question_id" : self.question_id,
            "id": self.answr_id,
            "answer": self.answer,
            "member_email" : self.current_user
            
        }
        answers.append(ansr)
        return answers