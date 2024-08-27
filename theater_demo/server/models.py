# create model (class) that represents our database table

#flask_sqlalchemy is our ORM extension
from flask_sqlalchemy import SQLAlchemy 
from sqlalchemy_serializer import SerializerMixin

db = SQLAlchemy()

class Production(db.Model, SerializerMixin):

    #this is the table name that will show up in resources.db (our SQL)
    __tablename__ = "productions"

    #columns that will show up in resources.db and that will be accessible as attributes (similarly to our attributes/properties from Phase 3)
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    title = db.Column(db.String)
    year = db.Column(db.Integer)
    director = db.Column(db.String)
    length = db.Column(db.Integer)

    #created_at and updated_at are great to have in the database, however may not necessarily be needed for our app.py routes' responses
    serialize_rules=('-created_at', '-updated_at')

    def __repr__(self):
        return f'<Production id={self.id} title={self.title} year={self.year} director={self.director} length={self.length} />'
