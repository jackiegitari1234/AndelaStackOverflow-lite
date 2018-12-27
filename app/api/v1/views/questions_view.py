
from app.api.v1.models.questions_model import quiz,questions
from flask import jsonify
from app.api.v1 import version1 as v1

@v1.route('/questions', methods=['GET'])
def fetch_questions():
    ''' Endpoint to fetch all questions'''

    if len(questions) == 0:
        return jsonify({"status": 200, "data": questions, "message": "No questions found"}), 200
    else:
        return jsonify({"status": 200, "data": questions}), 200