from sqlalchemy_serializer import SerializerMixin
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.ext.associationproxy import association_proxy

db = SQLAlchemy()

# productions has many roles
# roles belongs to productions

# actors has many roles
# roles belongs to an actors

# actors has many productions through roles
# productions has many actors through roles

# to migrate..
# flask db migrate (or flask db revision --autogenerate -m 'some message')
# flask db upgrade head 
class Production(db.Model, SerializerMixin):
    __tablename__ = "productions"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    #db.func.now() will give you the current DateTime
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

    #roles (list of role instances that align with this current production)
    #sqlalchemy will automate this process thanks to db.relationship and our foreign key
    # sqlalchemy level, do not have to migrate to database if we update relationship variable names
    characters = db.relationship('Role', back_populates='production')
    # list of Actor instances
    # Production.characters -> Role.actor
    cast = association_proxy('characters', 'actor')

    serialize_rules = ('-created_at', '-updated_at', '-characters.production', '-characters.actor', '-cast.movie_list', '-cast.repetoire')

    """
    {
        id,
        title,
        characters: [
            {
                id,
                role_name,
                production: [productions...],
                actor: [actors...]
            }
        ],
        cast: [
            id,
            name,
            repetoire: [roles...],
            movie_list: [productions...]
        ]
    }
    """
    


    def __repr__(self):
        return f'<Production {self.title} />'
    


class Actor(db.Model, SerializerMixin):
    __tablename__ = 'actors'

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    name = db.Column(db.String)
    country = db.Column(db.String)
    image = db.Column(db.String)
    age = db.Column(db.Integer)

    #roles - list of Role instances with the matching actor
    repetoire = db.relationship('Role', back_populates='actor')
    movie_list = association_proxy('repetoire', 'production')

    serialize_rules = ('-created_at', '-updated_at', '-repetoire.actor', '-movie_list.production', '-repetoire.production.characters')

    """
    {
        id,
        name,
        repetoire: [roles..., {
                id,
                role_name,
                production: {
                    id,
                    title,
                    cast,
                    characters
                },
                actor: {
                    id,
                    name,
                    repetoire,
                    movie_list
                }
            }],
        movie_list: [productions...,{
                id,
                title,
                characters: [
                    ...roles,
                    {
                        role_name,
                        production,
                        actor
                    }
                ],
                cast: [
                    ...actors
                ]
            }]
    }
    
    """
    
    

    def __repr__(self):
        return f'<Actor {self.name} />'

class Role(db.Model, SerializerMixin):

    __tablename__ = "roles"

    id = db.Column(db.Integer, primary_key=True)
    created_at = db.Column(db.DateTime, server_default=db.func.now())
    updated_at = db.Column(db.DateTime, onupdate=db.func.now())

    role_name = db.Column(db.String)
    production_id = db.Column(db.Integer, db.ForeignKey('productions.id'))
    actor_id = db.Column(db.Integer, db.ForeignKey('actors.id'))

    #production - one instance of the production that aligns with this role
    production = db.relationship('Production', back_populates='characters')

    #actor - one instance of the actor that aligns with this role
    actor = db.relationship('Actor', back_populates='repetoire')

    serialize_rules = ('-created_at', '-updated_at', '-actor.repetoire', '-production.characters')


    def __repr__(self):
        return f'<Role {self.role_name} />'
