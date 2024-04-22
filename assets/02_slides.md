---

title: ' '

---

# Intro to Flask-SQLAlchemy

---

## What We'll Be Doing

- Using SQL-Alchemy to connect Flask to a database

<aside class="notes">

- flask has no database abstraction layer  
- we can use an ORM extension - SQLAlchemy
- more specifically Flask-SQLAlchemy
</aside>

---

## Some Definitions

- ORM - object relational mapper.  It bridges the gap between databases and OOP based programs
- Schema Migration - the moving data to and from our database.  It also stores all previous versions of our database

<aside class="notes" >

- Flask SQL-Alchemy is for our ORM
- Flask Migrate is for our schema migration

</aside>

---

## Why Flask-SQLAlchemy and SQLAlchemy

- Flask does not have a built in database abstraction layer (ORM)
- Flask-SQLAlchemy is an extension that Flask can use to include an ORM

<aside class="notes" >

- There is also regular SQLAlchemy, Flask-SQLAlchemy is specifically for Flask and adds support for SQLAlchemy
- There is Flask-Migrate, Flask-Migrate uses Alembic
- So you will still be importing SQLAlchemy from Flask-SQLAlchemy, FlaskSQLAlchemy will just have a couple of other Flasky things

</aside>

---

## Why Flask-Migrate and Alembic

- We need a migration tool to be able to alter the databases we create
- Flask-Migrate uses Alembic to create templated scripts that tells our database how to alter itself (ex. drop tables, create, insert, update, delete, etc.)

<aside class="notes">

- Flask Migrate uses Alembic just as Flask-SQLAlchemy uses SQLAlchemy...these things are just Flask specific iterations
</aside>

---

## Using Flask-SQLAlchemy 

1. create a container that keeps track of features of a database (tables, columns, etc.)

```python
metadata = Metadata()
```

2. create a db object that uses said container
```python
db = SQLAlchemy(metadata=metadata)
```

<aside class="notes">

- this sets up our database to use with flask-sqlalchemy, the ORM
</aside>


---

## Connecting Flask with Flask-SQLAlchemy

1. create a Flask application
```python
app = Flask(__name__)
```

2. configure the database path you want a connection with
- database path is referred to as URI = Uniform Resource Identifier
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/db.db'
```

3. configure whether SQLAlchemy should track modifications to objects (inserts, updates, etc.)
```python
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
- this will use less memory

4. initialize the Flask application to use the database
```python
db.init_app(app)
```

<aside class="notes">

- flask is our API that will access the database via our ORM, flask-SQLAlchemy
</aside>


---

## Flask-SQLAlchemy [Configuration Keys](https://flask-sqlalchemy.palletsprojects.com/en/2.x/config/)

- There are a few other configuration keys such as...
<br />

`SQLALCHEMY_RECORD_QUERIES`: setting to record queries
<br />

`SQLALCHEMY_POOL_TIMEOUT`: speicfies connection timeout in seconds
<br />

`SQLALCHEMY_ECHO`: SQLAlchemy will log all errors if set to True

---



## Allowing schema migrations using Flask-Migrate

```python
migrate = Migrate(app, db)
```

- most of our work with Flask-Migrate will occur in terminal
```
> flask db init #creates directories for instance and migrations
> flask db migrate -m "Initial migration." #creates a migration script
> flask db upgrade head #upgrades the database to the most recent version
> flask db downgrade #downgrades to previous version
```
- you can also downgrade to any previous version of the database using the revision number

<aside class="notes">

- flask db history (shows list of migrations)
- flask db check - checks if any changes (like git status)
- https://flask-migrate.readthedocs.io/en/latest/
- when you make a change in your models' tables, you have to flask db migrate
- not all changes will be detectable (i think foreign keys?)

</aside>

---

## Models

- Models represent tables in your database 

```python
class Movie(db.Model):
    __tablename__ = 'movies'
    #primary_key=True is SQL specific, not a Python thing
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
```

---

## Creating with Flask-SQLAlchemy

1. Create a new instance
```python
movie = Movie(name="Ghostbusters")
```

2. Add new instance to the session (sessions handle the current batch of requests yet to be committed to the database)
```python
db.session.add(movie)
```

3. Commit those changes to the database (which actually changes the database)
```python
db.session.commit()
```

<aside class="notes">

- db.session.add() is like git add .
- db.session.commit() is like git commit
- you can do this in flask shell or in a file (such as a seed file)
</aside>

--- 

## Updating with Flask-SQLAlchemy

1. update the object
```python
movie.title = "Ghostbusters 2"
```

2. commit the update 
```python
db.session.commit()
```

---

## Deleting with Flask-SQLAlchemy

1. `db.session.delete(movie)`
2. `db.session.commit()`

---

## Reading with Flask-SQLAlchemy

`Movie.query.all()`
`Movie.query.first()`
`Movie.query.filter(Movie.title=="Ghostbusters").all()`

- More here: https://docs.sqlalchemy.org/en/20/orm/queryguide/query.html#the-query-object

---

## SerializerMixin

Having to write this again and again is annoying:

```python
for production in query:
    prods_list.append({
        "title": production.title,
        "genre": production.genre,
        "length": production.length
    })
```

---

## SerializerMixin

- Luckily we have `SerializerMixin`.
- We use `SerializerMixin` to automatically turn instances of our models into dictionaries:

```python
prods_list = []
for production in query:
    prods_list.append(production.to_dict())
```

- or even shorter...

```python
prods_list = [production.to_dict() for production in query]
```

---

## SerializerMixin

- Allows you to write rules on what fields to include in your response
- Especially helpful when you need to make use of relationships

```python
from sqlalchemy_serializer import SerializerMixin
from app import db

class SomeModel(db.Model, SerializerMixin)
```

- An easy way to serialize JSON for GET from db and for PUT/POST/PATCH/etc. from client.



---


## Serializer Rules

`serialize_only()` will include ONLY the exact specified fields
`serialize_rules()` is the negative to `serialize_only()` (so don't forget the `-`)

---

## Serializer Rules

```python
only_result = item.to_dict(only=('field_one', 'field_two'))
rules_result = item.to_dict(rules=('-field_one', '-field_two'))
```

OR

```python
serialize_only = ('field_one', 'field_two')
serialize_rules = ('-field_one', '-field_two')
```