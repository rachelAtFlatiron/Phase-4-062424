#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate 
from models import db, Production


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

db.init_app(app)

# | HTTP Verb 	|       Path       	| Description        	|
# |-----------	|:----------------:	|--------------------	|
# | GET       	|   /productions   	| READ all resources 	|
# | GET       	| /productions/:id 	| READ one resource   	|
# | POST      	|   /productions   	| CREATE one resource 	|
# | PATCH/PUT 	| /productions/:id 	| UPDATE one resource	|
# | DELETE    	| /productions/:id 	| DESTROY one resource 	|

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ✅ 1. Refactor `/productions` to include a `GET` and `POST`
@app.route('/productions')
def all_productions():
    q = Production.query.all()
    prod_list = [p.to_dict() for p in q]
    res = make_response(jsonify(prod_list), 200)
    return res 

    # ✅ 2. Create a route to /productions for a POST request
    # ✅ 2a. Get information from request.get_json() 
    # ✅ 2b. Create new object
    # ✅ 2c. Add and commit to db 
    # ✅ 2d. Convert to dictionary / # 5c. use .to_dict
    # ✅ 2e. Return as JSON
    # ✅ 2f. Test in postman

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ✅ 3. Create a delete request 
# ✅ 3a. Refactor `/productions/:id` to take both a `GET` and a `DELETE`
@app.route('/productions/<int:id>')
def One_Production(id):
    # ✅ 3b. Query for the wanted production
    q = Production.query.filter_by(id=id).first()
    prod_dict = q.to_dict()
    res = make_response(jsonify(prod_dict), 200)
    return res
    # ✅ 3c. Use `session.delete`
    # ✅ 4. PATCH request

if __name__ == '__main__':
    app.run(port=5555, debug=True)