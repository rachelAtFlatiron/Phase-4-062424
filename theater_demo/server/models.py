from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()
class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String) 
    genre = db.Column(db.String)
    length = db.Column(db.Integer) 
    year = db.Column(db.Integer) 
    image = db.Column(db.String)
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String) 
    composer = db.Column(db.String)


# ✅ 1. Create a Role model
    # ✅ 1a. Create a one-to-many relationship between `Role` and `Production`
    # ✅ 1b. Fetch the route `/productions` to see all the roles associated with each production
    # ✅ 1c. Create a `/roles` route to see the other side of the one-to-many relationship


# ✅ 2. Create an `Actor` model

    # ✅ 2a. Create a one-to-many relationship between `Role` and `Actor`
    # ✅ 2b. Fetch the route `/roles` to see all the roles associated with each actor
    # ✅ 2c. Create an `/actors` route to see the other side of the one-to-many relationship
    # ✅ 3. Create many-to-many relationship between `Production` and `Actor` using `association_proxy`
    # ✅ 3a. Use `SerializerMixin` to prevent max recursion
    # ✅ 3b. Create routes to access all actors and all productions

