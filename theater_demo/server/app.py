#!/usr/bin/env python3

from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate 
from models import db, Production, Role, Actor


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = 'sqlite:///app.db'
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False 

migrate = Migrate(app, db)

db.init_app(app)

@app.route('/')
def index():
    return '<h1>Hello World!</h1>'

@app.route('/productions')
def Productions():
    q = Production.query.all()
    prod_list = [p.to_dict() for p in q]

    res = make_response(jsonify(prod_list), 200)
    return res 

@app.route('/productions/<int:id>')
def One_Production(id):
    q = Production.query.filter_by(id=id).first()

    prod_dict = q.to_dict()
    res = make_response(jsonify(prod_dict), 200)
    return res

# ✅ 1c. Create a `/roles` route to see the other side of the one-to-many relationship
@app.route('/roles')
def all_roles():
    q = Role.query.all()

    role_dict = q.to_dict()
    res = make_response(jsonify(role_dict), 200)
    return res

# ✅ 3b. Create routes to access all actors and all productions
@app.route('/actors')
def all_actors():
    q = Actor.query.all()

    actor_dict = q.to_dict()
    res = make_response(jsonify(actor_dict), 200)
    return res

if __name__ == '__main__':
    app.run(port=5555, debug=True)