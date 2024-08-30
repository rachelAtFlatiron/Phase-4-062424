from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy
# 9a. import validates from sqlalchemy.orm
from sqlalchemy.orm import validates 
db = SQLAlchemy()

class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # constraints get triggered on db.session.commit()
    # constraints get triggered if you directly INSERT into db (i.e. in the sqlite3 shell)
    # however Flask will allow you to create instances that do not align with the constraints 
    title = db.Column(db.String, nullable=False) 
    genre = db.Column(db.String) 
    length = db.Column(db.Integer) 
    year = db.Column(db.Integer) 
    # every record has to have a unique image
    # there will be no repeated images
    image = db.Column(db.String, unique=True) 
    language = db.Column(db.String)
    director = db.Column(db.String)
    description = db.Column(db.String(20)) 
    composer = db.Column(db.String)

    roles = db.relationship('Role', back_populates='production')
    actors = association_proxy('roles', 'actor')
    
    serialize_rules = ('-created_at', '-updated_at', '-roles.production', '-actors.productions')

    # validations are flask only 
    # run when we create our instances
    # not affect if you directly INSERT into app.db via sqlite3 shell
    # 9b. validation: image must be 'png', 'jpg', or 'jpeg'

    # 9b. validation: year must be > 1850
    # these only get triggered when creating instances
    # if you directly insert into SQL we can put values < 1850
    @validates('year')
    def validates_year(self, key, user_year):
        if(user_year > 1850):
            return user_year 
        else: 
            raise ValueError('year must be greater than 1850')
        
    # 'image' refers to the column/attribute name
    @validates('image')
    def validate_image(self, key, user_image):
        if(user_image == ''):
            raise ValueError('image cannot be empty string')
        # image has to be .png, .jpeg, .jpg
        if('jpg' not in user_image and 'jpeg' not in user_image and 'png' not in user_image):
            raise ValueError('image must be of type jpeg, jpg, or png')
        return user_image

#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Actor(db.Model, SerializerMixin):
    __tablename__ = "actors"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    # CONSTRAINTS - sql level (will be triggered with db.session.add/commit)
    # name is required
    name = db.Column(db.String, nullable=False) 
    # image must be unique
    image = db.Column(db.String, unique=True) 
    age = db.Column(db.Integer)
    country = db.Column(db.String)

    roles = db.relationship('Role', back_populates='actor')
    productions = association_proxy('roles', 'production')

    serialize_rules = ('-created_at', '-updated_at', '-roles.actor', '-productions.actors')

    # age must be positive 
    @validates('age')
    def validate_age(self, key, user_age):
        if(user_age < 0):
            raise ValueError('human must be born')
        return user_age
    
    # 'image' refers to the column/attribute name
    @validates('image')
    def validate_image(self, key, user_image):
        if(user_image == ''):
            raise ValueError('image cannot be empty string')
        # image has to be .png, .jpeg, .jpg
        if('jpg' not in user_image and 'jpeg' not in user_image and 'png' not in user_image):
            raise ValueError('image must be of type jpeg, jpg, or png')
        return user_image

    
        
#~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

class Role(db.Model, SerializerMixin):
    __tablename__ = "roles"
    
    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())
   
    # 8c. add constraints
    role_name = db.Column(db.String, nullable=False) # 8c. required
    # 8d. test in sqlite3 and Postman
    
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'), nullable=False) # 8c. required
    production = db.relationship('Production', back_populates='roles')

    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'), nullable=False) # 8c. required
    actor = db.relationship('Actor', back_populates='roles')

    serialize_rules = ('-created_at', '-updated_at', '-production.roles', '-actors.roles')


