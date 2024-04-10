---

title: ' '

---

# Intro to Flask-SQLAlchemy

---

## What We'll Be Doing

- Using SQL-Alchemy to connect Flask to a database

<aside class="notes">
- front-end communicate with back-end <br />
- json-server was a really basic API <br />
- more complex APIs: data validation, authorization

</aside>

---

## Some Definitions

- ORM - object relational mapper.  It bridges the gap between databases and OOP based programs
- Data Migration - the moving data to and from our database.  It also stores all previous versions of our database

<aside class="notes" >
- Flask SQL-Alchemy is for our ORM
- Flask Migrate is for our data migration

</aside>

---

## Why Flask-SQLAlchemy and SQLAlchemy

- Flask does not have a built in database abstraction layer (ORM)
- Flask-SQLAlchemy is an extension that Flask can use to include an ORM

<aside class="notes" >
- There is also regular SQLAlchemy, Flask-SQLAlchemy is specifically for Flask and adds support for SQLAlchemy
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

## Initializing a Flask App

```python
app = Flask('mynameiswhat')
```

That's it!

---

## Connecting Flask with SQLAlchemy

1. configure the database path you want a connection with
- database path is referred to as URI = Uniform Resource Identifier
```python
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///path/to/db.db'
```
2. configure whether SQLAlchemy should track modifications to objects (inserts, updates, etc.)
```python
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
```
- this will use less memory
- we may get an error if we don't have this set

3. create an instance of the db 
```python
db = SQLALchemy(app)
```

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

## Creating a Route in Flask

Use a decorator!

```python
@app.route('/', methods=['GET', 'POST', ...])
def home():
    if request.method == 'GET':
        return {} 
```

---

## What do we send back?

### 🌈 JSON ✨
- We can add additional information to our response such as headers, status code, etc. with `make_response()`

---


## Request lifecycle
`@app.before_request`
`@app.after_request`
and more!...

```python
@app.before_request
def run_before():
    print('this is really useful when checking if a user is logged in')
```

---


## Context

- Application Context: Keeps track of current app's config variables, logger, database connections so that we don't have to pass the entire application instance from function to function

```python
    with app.app_context():
        # add seeds
```

- [Request Context](https://tedboy.github.io/flask/generated/generated/flask.Request.html): Keeps track of current request data such as URL, headers, method, request data, etc.

```python

from flask import request

# request.method
# request.get_json()
# request.args
# request.cookies
# request.base_url
# etc.

```

---

## Debugging

`import ipdb; ipdb.set_trace()`

<br />

`flask run --debug`
