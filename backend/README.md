# Full Stack Trivia API Backend

## Getting Started

### Installing Dependencies

#### Python 3.7

Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

#### Virtual Enviornment

We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

#### PIP Dependencies

Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:

```bash
pip install -r requirements.txt
```

This will install all of the required packages we selected within the `requirements.txt` file.

##### Key Dependencies

- [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

- [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

- [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

## Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

## Running the server

From within the `backend` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
export FLASK_APP=flaskr
export FLASK_ENV=development
flask run
```

Setting the `FLASK_ENV` variable to `development` will detect file changes and restart the server automatically.

Setting the `FLASK_APP` variable to `flaskr` directs flask to use the `flaskr` directory and the `__init__.py` file to find the application. 

## Tasks

One note before you delve into your tasks: for each endpoint you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 
2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 
3. Create an endpoint to handle GET requests for all available categories. 
4. Create an endpoint to DELETE question using a question ID. 
5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 
6. Create a POST endpoint to get questions based on category. 
7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 
8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 
9. Create error handlers for all expected errors including 400, 404, 422 and 500. 

REVIEW_COMMENT
```
This README is missing documentation of your endpoints. Below is an example for your endpoint to get all categories. Please use it as a reference for creating your documentation and resubmit your code. 

Endpoints
GET '/categories'
GET ...
POST ...
DELETE ...

GET '/categories'
- Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
- Request Arguments: None
- Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 
{'1' : 'Science',
'2' : 'Art',
'3' : 'Geography',
'4' : 'History',
'5' : 'Entertainment',
'6' : 'Sports'}

```
API Documentation
 GETTING STARTED:
 Base URL: This project based locally at http://127.0.0.1:5000/
 Authentication: This project at this moment has no require authentication or API keys

 ERROR HANDLING:
  Errors should usually be returned in JSON format
        example:
        {
            'success': False,
            'error': 404,
            'message': 'resource not found'
        }
    This API returns two types of errors::
    404-resource not found
    422-unprocessable
 ENDPOINTS:
 GET 'category':
        1.Returns a dictionary of categories
        2.example:curl -X http://127.0.0.1:5000/categories
                            {
                        'categories': {
                            '1': 'Science', 
                            '2': 'Art', 
                            '3': 'Geography', 
                            '4': 'History', 
                            '5': 'Entertainment', 
                            '6': 'Sports'
                        }, 
                        'success': true
                    }
 GET 'questions':
        1.Returns a dictionary of questions and dictionary of categories
        2.Results are paginated in groups of 10.
        3.example:curl -X http://127.0.0.1:5000/questions
                         {
                        'categories': {
                            '1': 'Science', 
                            '2': 'Art', 
                            '3': 'Geography', 
                            '4': 'History', 
                            '5': 'Entertainment', 
                            '6': 'Sports'
                        }, 
                        'questions': [
                            {
                                'answer': 'Some answer', 
                                'category': 3, 
                                'difficulty': 3, 
                                'id': 1, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 1, 
                                'id': 2, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 1, 
                                'difficulty': 4, 
                                'id': 3, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 6, 
                                'difficulty': 4, 
                                'id': 4, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 4, 
                                'difficulty': 3, 
                                'id': 5, 
                                'question': some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 3, 
                                'id': 6, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 4, 
                                'id': 7, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 4, 
                                'difficulty': 2, 
                                'id': 8, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 1, 
                                'difficulty': 2, 
                                'id': 9, 
                                'question': 'What is the largest lake in Africa?'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 3, 
                                'difficulty': 3, 
                                'id': 10, 
                                'question': 'some question'
                            }
                        ], 
                        'success': true, 
                        'total_questions': 30
                    }
DELETE 'questions/<question_id>':
        1.Delete selected question
        2.returns Result of deleted question and status of success
        3.example curl -X DELETE http://127.0.0.1:5000/questions/2
                    {
                        'deleted': 2, 
                        'success': true
                        'questions': current_questions,
                        'total_questions': len(selection)
                    }

POST 'questions':
    This endpoint creates a new question and also might include a search result
    IF there's no search_term in request:
        1.creates new question using JSON format
        2.Returns JSON-result of Request Body' question, answer, difficulty and category' and status of success
        3.Returns total of paginated questions
        4.Example curl -X POST http://127.0.0.1:5000/questions -H 'Content-Type: application/json' -d '{ 'question': 'test question', 'answer': 'test answer', 'difficulty': 1, 'category': '1' }
                    {
                        'created': 11, 
                        'question_created': 'test question'
                        'questions': [
                            {
                                'answer': 'Some answer', 
                                'category': 3, 
                                'difficulty': 3, 
                                'id': 1, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 1, 
                                'id': 2, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 1, 
                                'difficulty': 4, 
                                'id': 3, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 6, 
                                'difficulty': 4, 
                                'id': 4, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 4, 
                                'difficulty': 3, 
                                'id': 5, 
                                'question': some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 3, 
                                'id': 6, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 4, 
                                'id': 7, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 4, 
                                'difficulty': 2, 
                                'id': 8, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 1, 
                                'difficulty': 2, 
                                'id': 9, 
                                'question': 'What is the largest lake in Africa?'
                            }, 
                            {
                                'answer': 'test question', 
                                'category': 1, 
                                'difficulty': 1, 
                                'id': 11, 
                                'question': 'test answer'
                            }
                        ], 
                        'success': true, 
                        'total_questions': 31
                    }
    IF there's search_term in request:
        1.Searches for questions using search term in JSON format.
        2.Returns JSON format with paginated selected questions.
        3.example: curl -X http://127.0.0.1:5000/questions -H 'Content-Type: application/json' -d '{'searchTerm': 'test question'}'
                    {
                        'questions': [
                            {
                                'answer': 'test question', 
                                'category': 1, 
                                'difficulty': 1, 
                                'id': 11, 
                                'question': 'test answer'
                            }, 
                        ], 
                        'success': true, 
                        'total_questions': 31
                    }
GET 'categories/<int:category_id>/questions'
        1.This request returns list of questions based on category
        2.This request requires arguments: Category Id and Page Number.
        3.example curl -X http://127.0.0.1:5000/categories/2/questions
                      {
                        'current_category': 'Art', 
                        'questions': [
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 2, 
                                'id': 9, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 3, 
                                'id': 6, 
                                'question': 'some question'
                            }, 
                            {
                                'answer': 'Some answer', 
                                'category': 2, 
                                'difficulty': 4, 
                                'id': 7, 
                                'question': 'some question'
                            }
                        ], 
                        'success': true, 
                        'total_questions': 31
                    }
POST 'quizzes'
    1.This request allows us to get a questions to play the quiz
    2.Uses JSON format for category and previous question
    3.examples: curl -X -POST http://127.0.0.1:5000/quizzes -H 'Content-Type: application/json' -d '{'previous_questions': [15, 16], 'quiz_category': {'type': 'Science', 'id': '1'}}'
                     {
                        'question': {
                            'answer': 'Some answer', 
                            'category': 1, 
                            'difficulty': 4, 
                            'id': 17, 
                            'question': 'some question'
                        }, 
                        'success': true
                    }
    
Author
    Ermakov David, student of Full-stack Web Developer programm in Udacity, created API and wrote this Documentation


## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```