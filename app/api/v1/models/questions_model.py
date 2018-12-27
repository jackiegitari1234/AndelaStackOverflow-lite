questions = [
    {
        "id" : 1,
        "question" : "what is java?"
    },
    {
        "id" : 2, 
        "question" : "what is a compiler?",
    }
]
class quiz(object):    
    '''This class initializes User Model and Stores User Credential'''
    
    def __init__(self, question=None):
        self.quiz_id = len(questions)+1
        self.question = question