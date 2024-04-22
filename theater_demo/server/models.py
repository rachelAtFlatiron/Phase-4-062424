# handle creating the database

#SQLAlchemy import
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()
# 1. ✅ Create a Production Model
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

    # ✅ 9b. Use serializer rules to remove `created_at` and `updated_at`
    serialize_rules = ('-created_at', '-updated_at')
# ✅ 2. navigate to app.py