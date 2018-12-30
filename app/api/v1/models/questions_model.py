questions = [
    {
        "id" : 1,
        "owner_id" : 1,
        "question" : "what is java?"
    },
    {
        "id" : 2, 
        "owner_id" : 2,
        "question" : "what is a compiler?",
    }
]
answers = [
    {
        "id" : 1,
        "question_id" : 1,
        "member_id" : 3,
        "answer" : "A programming language"
    },
    {
        "id" : 2, 
        "question_id" : 1,
        "member_id" : 2,
        "answer" : "A server side programming language"
    }
]
class quiz(object):    
    
    def __init__(self, question=None):
        self.quiz_id = len(questions)+1
        self.question = question

    def add_quiz(self):
        quiz = {
            "id": self.quiz_id,
            "question": self.question
        }
        questions.append(quiz)
        return questions

class answer(object):    
    
    def __init__(self, answer=None,question_id=None):
        self.answr_id = len(questions)+1
        self.question_id = question_id
        self.answer = answer

    def add_answer(self):
        answr = {
            "question_id" : self.question_id,
            "id": self.answr_id,
            "answer": self.answer
            
        }
        answers.append(answr)
        return answers