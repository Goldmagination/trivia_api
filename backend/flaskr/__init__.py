import os
from flask import Flask, request, abort, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import random

from models import setup_db, Question, Category

QUESTIONS_PER_PAGE = 10


def paginate_questions(request, selection):
    page = request.args.get('page', 1, type=int)
    start = (page - 1) * QUESTIONS_PER_PAGE
    end = start + QUESTIONS_PER_PAGE

    questions = [question.format() for question in selection]
    current_questions = questions[start:end]

    return current_questions


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__)
    setup_db(app)
    CORS(app)

    '''
  @TODO: Set up CORS. Allow '*' for origins. Delete the sample route after completing the TODOs
  '''
    @app.after_request
    def after_request(response):
        response.headder.add('Access-Control-Allow-Headers',
                             'Content-Type, Authorization ')
        response.headder.add('Access-Control-Allow-Methods',
                             'GET, POST, PATCH, OPTIONS, DELETE ')
        return response

    '''
  @TODO: Use the after_request decorator to set Access-Control-Allow
  '''
    @app.route(('/categories'), Methods=['GET'])
    def get_categories():
        available_categories = Category.query.all()
        formated_catogories = [Category.format()
                               for category in available_categories]

        if len(formated_catogories) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'categories': formated_catogories,
            'total categories': len(formated_catogories)
        })
    '''
  @TODO:
  Create an endpoint to handle GET requests
  for all available categories.
  '''
    @app.route('/questions', Methods=['GET'])
    def get_questions():
        selection = Question.query.order_by(Question.id).all()
        current_questions = paginate_questions(request, selection)
        categories_d = {}
        for category in selection:
            categories_dict[category.id] = category.type

        if len(current_questions) == 0:
            abort(404)

        return jsonify({
            'success': True,
            'questions': current_questions,
            'total_questions': len(selection),
            'categories': categories_d,
        })
    '''
  @TODO:
  Create an endpoint to handle GET requests for questions,
  including pagination (every 10 questions).
  This endpoint should return a list of questions,
  number of total questions, current category, categories.

  TEST: At this point, when you start the application
  you should see questions and categories generated,
  ten questions per page and pagination at the bottom of the screen for three pages.
  Clicking on the page numbers should update the questions.
  '''

    '''
  @TODO:
  Create an endpoint to DELETE question using a question ID.

  TEST: When you click the trash icon next to a question, the question will be removed.
  This removal will persist in the database and when you refresh the page.
  '''
    @app.route('/questions/<int:question_id>', methods=['DELETE'])
    def delete_question(id):
        try:
            question = Question.query.filter(
                Question_id == question_id).one_or_none()

            if question is None:
                abort(404)

            question.delete()
            selection = Question.query.order_by(Question.id).all()
            current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'deleted_question': question_id,
                'questions': current_questions,
                'total_questions': 'len(selection)'
            })
        except:
            abort(422)
    '''
  @TODO:
  Create an endpoint to POST a new question,
  which will require the question and answer text,
  category, and difficulty score.

  TEST: When you submit a question on the 'Add' tab,
  the form will clear and the question will appear at the end of the last page
  of the questions list in the 'List' tab.
  '''
    @app.route('/questions', methods=['POST'])
    def add_question():
        body = request.get_json()

        new_question = body.get('question', None)
        new_answer = body.get('answer', None)
        new_category = body.get('category', None)
        new_difficulty = body.get('difficulty', None)
        try:
            if (body.get('searchTerm')):
                search_term = body.get('searchTerm')
                selection = Question.query.order_by(Question.id).filter(
                    Question.question.ilike('%{}%'.format(search_term)))
                current_questions = paginate_questions(request, selection)

                return jsonify({
                    'success': True,
                    'created': question.id,
                    'questions': current_questions,
                    'total_questions': len(selection)
                })
            else:
                question = Question(question=new_question, answer=new_answer,
                                    category=new_category, difficulty=new_difficulty)
                question.insert()

                selection = Question.query.order_by(Question.id).all()
                current_questions = paginate_questions(request, selection)

            return jsonify({
                'success': True,
                'created': question.id,
                'questions': current_questions,
                'total_questions': len(selection)
            })
        except:
            abort(422)
    '''
  @TODO:
  Create a POST endpoint to get questions based on a search term.
  It should return any questions for whom the search term
  is a substring of the question.

  TEST: Search by any phrase. The questions list will update to include
  only question that include that string within their question.
  Try using the word 'title' to start.
  '''
    @app.route('/category/<int:category_id>/questions', methods=['GET'])
    def get_question_by_category(category_id):
        category = Category.query.filter_by(
            category_id=category_id).one_or_none()

        if category is None:
            abort(404)

        selection = Question.query.filter_by(category=category.id).all()
        paginated_question = paginate_questions(request, selection)
        return jsonify({
            'success': True,
            'questions': paginated_question,
            'total_questions': len(selection),
            'current_category': category
        })

    '''
  @TODO: 
  Create a GET endpoint to get questions based on category. 

  TEST: In the 'List' tab / main screen, clicking on one of the 
  categories in the left column will cause only questions of that 
  category to be shown. 
  '''
    @app.route('/quizzes', methods=['POST'])
    def get_random_quiz_question():
        body = request.get_json()
        previous = body.get('previous_questions')
        category = body.get('quiz_category')
        if category is None or previous is None:
            abort(404)
        if category['id'] == 0:
            questions = Question.query.all()
        else:
            questions = Question.query.filter_by(category=category['id']).all()
        total = len(questions)

        def get_random_question():
            return questions[random.randrange(0, len(questions), 1)]

        def check_used(question):
            used = False
            for q in previous:
                if (q == question.id):
                    used = True

            return used

        question = get_random_question()
        while (check_if_used(question)):
            question = get_random_question()
            if (len(previous) == total):
                return jsonify({
                    'success': True
                })
        return jsonify({
            'success': True,
            'question': question.format()
        })
    '''
  @TODO: 
  Create a POST endpoint to get questions to play the quiz. 
  This endpoint should take category and previous question parameters 
  and return a random questions within the given category, 
  if provided, and that is not one of the previous questions. 

  TEST: In the 'Play' tab, after a user selects 'All' or a category,
  one question at a time is displayed, the user is allowed to answer
  and shown whether they were correct or not. 
  '''

    '''
  @TODO: 
  Create error handlers for all expected errors 
  including 404 and 422. 
  
  '''
    @app.errorhandler(404)
    def not_found(error):
        return jsonify({
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }), 404

    @app.errorhandler(422)
    def unprocessable(error):
        return jsonify({
            'success': False,
            'error': 422,
            'message': 'unprocessable'
        }), 422

    return app
