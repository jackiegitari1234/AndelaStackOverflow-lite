
from app.api.v1.models.questions_model import quiz,questions,answers,answer
from flask import jsonify,request
from app.api.v1 import version1 as v1
from app.api.v1.utils.validator import token_check


#fetch all questions
@v1.route('/questions', methods=['GET'])
@token_check
def fetch_questions(current_user):
    ''' Endpoint to fetch all questions'''

    if len(questions) == 0:
        return jsonify({"status": 200, "data": questions, "message": "No questions found"}), 200
    else:
        return jsonify({"status": 200, "data": questions}), 200

#post a question
@v1.route('/questions', methods=['POST'])
@token_check
def post_question(current_user):

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["question"]):
        return jsonify({"status": 400, "message": "Please type-in a question"}), 400

    question = data['question']
    current_user = current_user

    question = quiz(question,current_user).add_quiz() #append question
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
@token_check
def post_answer(current_user,id):

    # Check for json data
    data = request.get_json()

    if not data:
        return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
    
    # Check for empty inputs
    if not all(field in data for field in ["answer"]):
        return jsonify({"status": 400, "message": "Please type-in an answer"}), 400

    answr = data['answer']
    question_id = id
    current_user = current_user

    quiz = [question for question in questions if question["id"] == id]
    if quiz:
        answ = answer(answr,question_id,current_user).add_answer() #append answer
        answr = [answer for answer in answ if answer["question_id"] == id]
        return jsonify({"status": 201,"answers" : answr})
    return jsonify({"status":400, "message": "No question with id {} found".format(id)}), 400

#delete a question
@v1.route('/questions/<int:id>', methods=['DELETE'])
@token_check
def delete_quiz(current_user,id):
    current_user = current_user
    qstn = [question for question in questions if question["id"] == id]
    owner = [question for question in questions if question["owner_email"] == current_user]
    if qstn:
        if owner:
            questions.remove(qstn[0])
            return jsonify({"status": 200, "question": questions})
        return jsonify({"status":400,"message":"previlige denied"})
    return jsonify({"status":400, "message": "No question with id {} found".format(id)}), 400

#modify an answer to a question
@v1.route('/questions/<int:questionId>/answers/<int:answerId>', methods=['PUT'])
@token_check
def update_answer(current_user,questionId,answerId):
    current_user = current_user
    qstn = [question for question in questions if question["id"] == questionId]
    answer = [answer for answer in answers if answer["question_id"] == questionId if answer["id"] == answerId]
    owner = [question for question in questions if question["id"] == questionId if question["owner_email"] == current_user]
    commentor = [answer for answer in answers if answer["question_id"] == questionId if answer["member_email"] == current_user if answer["id"] == answerId]
    allanswers = [answer for answer in answers if answer["question_id"] == questionId]

    if qstn:
        if owner:
            if answer:
                data = request.get_json()
                if not data:
                    return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
                if not all(field in data for field in ["answer"]):
                    return jsonify({"status": 400, "message": "Mark the answer as best"}), 400
                qstn[0]['status'] = data['status']
                return jsonify({"status": 200, "message": qstn})
            return jsonify({"status": 200,"answers":"not a valid answer"})

        if commentor:
            data = request.get_json()
            if not data:
                return jsonify({"status": 400, "message": "POST of type Application/JSON expected"}), 400
            if not all(field in data for field in ["answer"]):
                return jsonify({"status": 400, "message": "Please type-in a answer"}), 400
            commentor[0]['answer'] = data['answer']
            return jsonify({"status": 200, "answers": allanswers})
        return jsonify({"message": "user not authorised"})

    return jsonify({"status":400, "message": "No question with id {} found".format(questionId)}), 400
    