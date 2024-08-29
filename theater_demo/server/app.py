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
    return jsonify({"message": "welcome to the productions api"})

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ✅ 1. Refactor `/productions` to include a `GET` and `POST`
@app.route('/productions', methods=["GET", "POST"])
def all_productions():
    if(request.method == "GET"):
        q = Production.query.all()
        #NEED TRAILING COMMA IF THERE'S ONLY ONE RULE
        #THE RULES TAKES A TUPLE
        prod_list = [p.to_dict(rules=('-roles', )) for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    if(request.method == "POST"):
        # get values provided by user

        #request.args -> put args in URL query (.../productions?key1=value1)
        #request.form -> use body > form-data field in POSTMAN (or update headers for fetch request on client side)
        #request.get_json() -> use body > raw (set to JSON) in POSTMAN (or update headers for fetch request on client side)
        data = request.get_json()

        # create new Production instance using said values
        try:
            #using .get() so that Python doesn't break if that key/value pair does not exist (data.get('non-existing-key') => None)
            #using data['key'] -> if the key does not exist code will break (KeyError)
            prod = Production(title=data.get("title"), genre=data.get("genre"),length=data.get("length"),year=data.get("year"),image=data.get("image"),language=data.get("language"),director=data.get("director"),description=data.get("description"), composer=request.args.get("composer"))
        except:
            #422 - unprocessable entity
            return jsonify({"message": "include values for all fields"}), 422
        db.session.add(prod)
        db.session.commit()
        # add/commit new Production instance to database
        # return new instance as JSON response
        return jsonify(prod.to_dict()), 201

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
#delete request goes here since we need the id of the record that we want to delete
@app.route('/productions/<int:id>', methods=["GET", "DELETE", "PATCH"])
def one_production(id):
    #get the relevant production instance (whether for get, delete, patch)
    q = Production.query.filter_by(id=id).first()
    # import ipdb; ipdb.set_trace()
    # error handling
    if(not q):
        return jsonify({"message": f'production {id} not found'}), 404
    if(request.method == "GET"):
        prod_dict = q.to_dict()
        res = make_response(jsonify(prod_dict), 200)
        return res
    if(request.method == "DELETE"):
        #use our orm 
        db.session.delete(q)
        #commit to database
        db.session.commit()
        #return an empty response (as is customary)
        return jsonify({}), 204
    if(request.method == "PATCH"):
        
        try:
            data = request.get_json()
            #patch requests we don't know what fields the user included, so we have to dynamically update fields
            # loop through our data dictionary
            for cur_field in data: 
                # use setattr
                setattr(q, cur_field, data.get(cur_field))
            db.session.add(q)
            db.session.commit()
        except: 
            return jsonify({"message": f"something went wrong with PATCH /productions {id}"}), 422

        return jsonify(q.to_dict(), 200)



if __name__ == '__main__':
    app.run(port=5555, debug=True)