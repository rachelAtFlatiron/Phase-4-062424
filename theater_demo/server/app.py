#!/usr/bin/env python3

# 1a. Set Up Imports
from flask import Flask, jsonify, make_response, request
# 1b. Create instance of Flask
app = Flask(__name__)

#in terminal
# export FLASK_APP=app.py
# export FLASK_RUN_PORT=5555
# flask run --debug

global id 
id = 3

#default is GET
@app.route('/')
def index():
    return {
        'value': 'hello world'
    }

@app.route('/longest-movies')
def get_longest_movies():
    prod = {
        "title": "immitation game",
        "genre": "drama",
        "length": 120
    }
    make_response_prod = make_response(prod, 200)
    print(type(make_response_prod))
    #return prod -> returns dict
    #jsonify(prod) -> returns flask response object instance
    #make_response(prod) -> returns flask response object instance
    return make_response_prod

# keep in mind that spaces will be converted to ascii: %20
@app.route('/productions/<string:title>')
def production_by_title(title):
    print(title)
    prod = {
        "title": title 
    }
    return jsonify(prod), 200

@app.route('/productions/<int:length>')
def production_by_length(length):
    return jsonify({
        "movie_length": length
    }), 200

# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`
@app.route('/my_context')
def my_context():
    #display request information
    #mostly using request to access json passed in via POST requests
    #import ipdb; ipdb.set_trace()
    global id
    id = 5
    print("returning my_context result")
    return jsonify({
        "path": request.path,
        "host": request.host,
        # request.method is helpful
        "method": request.method
    }), 200

# very helpful when handling users and sessions within Flask
# not part of CC, we will be covering users/sessions post CC
@app.before_request
def runs_before():
    print("before request", id)

@app.after_request 
def runs_after(response):
    print("after request", id)
    # don't forget to return the response 
    return response

#run app.py (make sure you're in the right folder)
if __name__ == '__main__':
    app.run(port=5555, debug=True)