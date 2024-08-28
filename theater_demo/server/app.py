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
def all_productions():
    q = Production.query.all()
    prod_list = [p.to_dict(only=('title', 'id', 'year')) for p in q]

    res = make_response(jsonify(prod_list), 200)
    return res 

@app.route('/productions/<int:id>')
def production_by_id(id):
    q = Production.query.filter_by(id=id).first()

    prod_dict = q.to_dict()
    res = make_response(jsonify(prod_dict), 200)
    return res

@app.route('/actors')
def all_actors():
    q = Actor.query.all()
    actor_dict = [a.to_dict() for a in q]
    return jsonify(actor_dict), 200

@app.route('/roles/<int:role_id>')
def role_by_id(role_id):
    q = Role.query.filter_by(id=role_id).first()
    return jsonify(q.to_dict()), 200

@app.route('/roles')
def all_roles():
    q = Role.query.all()
    q_dict = [role.to_dict() for role in q]
    return jsonify(q_dict), 200

if __name__ == '__main__':
    app.run(port=5555, debug=True)