
from app.api.v1.models.questions_model import quiz,questions,answers,answer
from flask import jsonify,request
from app.api.v1 import version1 as v1

#fetch all questions
@v1.route('/questions', methods=['GET'])
def fetch_questions():
    ''' Endpoint to fetch all questions'''

    if len(questions) == 0:
        return jsonify({"status": 200, "data": questions, "message": "No questions found"}), 200
    else:
        return jsonify({"status": 200, "data": questions}), 200

#post a question
@v1.route('/questions', methods=['POST'])
def post_question():

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["question"]):
        return jsonify({"status": 400, "message": "Please type-in a question"}), 400

    question = data['question']

    question = quiz(question).add_quiz() #append question
    return jsonify(question), 201


#fetch a specific question with answers
@v1.route('/questions/<int:id>', methods=['GET'])
def get_quiz(id):
    quiz = [question for question in questions if question["id"] == id]
    answr = [answer for answer in answers if answer["question_id"] == id]

    if quiz:
        if answr:
            return jsonify({"status": 200, "question": quiz[0],"answers" : answr})
        return jsonify({"status": 200, "question": quiz[0],"answers":"no answers yet"})
    return jsonify({"status":400, "message": "No question with id {} found".format(id)}), 400

#post an answer to a question
@v1.route('/questions/<int:id>/answer', methods=['POST'])
def post_answer(id):

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["answer"]):
        return jsonify({"status": 400, "message": "Please type-in an answer"}), 400

    answr = data['answer']
    question_id = id

    quiz = [question for question in questions if question["id"] == id]
    if quiz:
        answ = answer(answr,question_id).add_answer() #append answer
        answr = [answer for answer in answ if answer["question_id"] == id]
        return jsonify({"status": 201,"answers" : answr})
    return jsonify({"status":400, "message": "No question with id {} found".format(id)}), 400

#delete a question
@v1.route('/questions/<int:id>', methods=['DELETE'])
def delete_quiz(id):
    quiz = [question for question in questions if question["id"] == id]
    if quiz:
        questions.remove(quiz[0])
        return jsonify({"status": 200, "question": questions})
    return jsonify({"status":400, "message": "No question with id {} found".format(id)}), 400