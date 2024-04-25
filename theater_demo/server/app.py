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
@app.route('/productions', methods=["GET", "POST"])
# 🛑 emphasize class name needs to be different from model name
def Productions():
    if(request.method=="GET"):
        q = Production.query.all()
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    #request.form for x-www-form-urlencoded, multipart/form
    #request.args for params in url 
    #request.get_json() or request.json for JSON
    #request.values for both form and params - since both are one long query string

    if(request.method=="POST"):
        # ✅ 2. Create a route to /productions for a POST request
        # 🛑 possible headers:
            # multipart/form-data: header content-type: multipart/form-data
                # good for files, non-ASCII, binary data, large data
                # contains some sort of boundary?
            # www-form-urlencoded: content-type: x-www-form-urlencoded
                # use for simple text fields, body is essentially one giant query string
            # raw json: content-type: application/json

        # 🛑 request.form: key value pairs x-www-form-urlencoded or form-data (changes content-type header))
            
        # 🛑 request.json or request.get_json() - for json (you will use this because you will be setting those headers in your POST request)
            # must choose either json or x-www-form-urlencoded as per headers

        # 🛑 request.args: gets from params (which you see in the URL)

        # 🛑 request.values: gets from body and params
        
        # ✅ 2a. Get information from request.get_json() 
        data = request.get_json()
        # ✅ 2b. Create new object
        prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
        # ✅ 2c. Add and commit to db 
        db.session.add(prod)
        db.session.commit()
        # ✅ 2d. Convert to dictionary / # 5c. use .to_dict

        # dict = {
        #     "id": prod.id,
        #     "title": prod.title
        # }

        dict = prod.to_dict()
        
        # ✅ 2e. Return as JSON
        return make_response(jsonify(dict), 201)
        # ✅ 2f. Test in postman

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# ✅ 3. Create a delete request 
# ✅ 3a. Refactor `/productions/:id` to take both a `GET` and a `DELETE`
@app.route('/productions/<int:id>', methods=["GET", "DELETE", "PATCH"])
def One_Production(id):
    # ✅ 3b. Query for the wanted production
    q = Production.query.filter_by(id=id).first()
    if not q:
        return make_response({'message': 'production not found'}, 404)
        # can also use werkzeug HTTP exception
        # from werkzeug.exceptions import HTTPException, NotFound
        # raise NotFound()
    if(request.method == 'GET'):
        prod_dict = q.to_dict()
        res = make_response(jsonify(prod_dict), 200)
        return res

    if(request.method == "DELETE"):
        q = Production.query.filter_by(id=id).first()
        # ✅ 3c. Use `session.delete`
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
    
    if(request.method == "PATCH"):
        
        json_dict = request.get_json()
        #request.form for x-www-form-urlencoded, multipart/form
        #request.args for params in url 
        #request.get_json() or request.json for JSON
        #request.values for both form and params - since both are one long query string
        for attr in json_dict:
            setattr(q, attr, json_dict.get(attr))
        db.session.add(q)
        db.session.commit()
        return make_response(q.to_dict(), 200)

if __name__ == '__main__':
    app.run(port=5555, debug=True)