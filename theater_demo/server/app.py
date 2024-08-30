#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request, abort
from flask_migrate import Migrate 
from models import db, Production, Role, Actor
from flask_restful import Api, Resource



app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

#work with api to add resources/endpoints (api.add_resource(...))
api = Api(app)


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

@app.route('/productions', methods=["GET", "POST"])
#class AllProductions(Resource): pass
#api.add_resource(AllProductions, '/productions)
def all_productions():
    if(request.method=="GET"): #def get(self):
        q = Production.query.all()
        prod_list = [p.to_dict() for p in q]
        res = make_response(jsonify(prod_list), 200)
        return res 
    
    if(request.method=="POST"):
        data = request.get_json()
        prod = Production(title=data.get('title'), genre=data.get('genre'), length=data.get('length'), year=data.get('year'), image=data.get('image'), language=data.get('language'), director=data.get('director'), description=data.get('description'), composer=data.get('composer') )
        db.session.add(prod)
        db.session.commit()

        dict = prod.to_dict()
        return make_response(jsonify(dict), 201)

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#@app.route('/productions/<int:id>', methods=["GET", "DELETE"])
class OneProduction(Resource):
#def one_production(id):
    #if(request.method == 'GET'):
    def get(self, id):
        q = Production.query.filter_by(id=id).first()
        prod_dict = q.to_dict()
        res = make_response(jsonify(prod_dict), 200)
        return res

    #if(request.method == "DELETE"):
    def delete(self, id):
        q = Production.query.filter_by(id=id).first()
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)
api.add_resource(OneProduction, '/productions/<int:id>')

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

# /roles
# get, post to /roles

#'Roles' is an arbitrary classname HOWEVER it cannot match your model name
#if it matches your model name, it will overwrite the model
class Roles(Resource):

    #method names have to align with http verb
    def get(self):
        q = Role.query.all()
        #iteration over each Role instance returned to us by the query
        #using SerializerMixin's .to_dict() to turn that instance into a dictionary
        #we are also passing in 'only' options to .to_dict to specify which individual fields we want in said dictionary
        if(not q):
            return make_response({"message": "/roles not found"}, 404)
        role_dict = [r.to_dict(only=('id', 'role_name', 'production.title')) for r in q]
        # USE MAKE_RESPONSE FOR FLASK_RESTFUL
        return make_response(role_dict, 200)

    def post(self):
        data = request.get_json()
        try:
            role = Role(role_name=data.get("role_name"), production_id=data.get("production_id"), actor_id=data.get("actor_id"))
            db.session.add(role)
            db.session.commit()
            return make_response(role.to_dict(), 201)
        except:
            return make_response({"message": "something went wrong POST /roles"}, 422)

# actually create the endpoint
api.add_resource(Roles, '/roles')

# PATCH/DELETE/GET
class One_Role(Resource):

    def helper_get(self, id):
        q = Role.query.filter_by(id=id).first()
        if(not q):
            return make_response({"message": f'role {id} not found'}, 404)
        return q
    
    def get(self, id):
        q = self.helper_get(id)
        return make_response(q.to_dict(), 200)

    def patch(self, id):
        q = self.helper_get(id)
        try: 
            data = request.get_json()
            #update the instance
            for cur_field in data:
                setattr(q, cur_field, data.get(cur_field))
            db.session.add(q)
            db.session.commit()
            return make_response(q.to_dict(), 200)
        except:
            return make_response({"message": "patch went wrong"}, 422)


    def delete(self, id):
        q = self.helper_get(id)
        db.session.delete(q)
        db.session.commit()
        return make_response({}, 204)

api.add_resource(One_Role, '/roles/<int:id>')

# DO NOT DO THE FOLLOWING
# reassigning the model class Actor to the resource class Actor
# resource classes do not have .query
# error: AttributeError: type object 'Actor' has no attribute 'query'
class Actor(Resource):
    def get(self):
        q = Actor.query.all()
        return make_response([a.to_dict(only=('name', 'id')) for a in q], 200)
api.add_resource(Actor, '/actors')

if __name__ == '__main__':
    app.run(port=5555, debug=True)