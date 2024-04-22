# Intro to Flask-SQLAlchemy

## SWBATs

- [ ] Use Flask-SQLAlchemy as an ORM
- [ ] Use Flask-Migrate to manage database schemas
- [ ] Initialize a database with sample data
- [ ] Implement a Flask application to query a database

---

## Deliverables

### 1. In `models.py` create a Production Model 
#### - Use the tablename `productions`
#### - Include columns title: string, genre: string, budget:float, image:string,director: string, description:string, ongoing:boolean, created_at:date time, updated_at: date time 

<br />

---

<br />

### 2. Set up a flask app in `app.py`
#### 2a. In `app.py` import flask, migrate, db, and the Production model
#### 2b. Create an instance of a flask app
#### 2c. Configure the flask app to connect to a database 
#### 2d. Enable Alembic using `Migrate`
#### 2e. Connect app with backend

<br />

---

<br />

### 3. Migrate the `Production` model using flask

<br />

---

<br />

### 4. Create a `seed.py` file
#### 4a. Import app, db, and models
#### 4b. Create application context 
#### 4c. Delete all existing records before reseeding
#### 4d. Create some seeds and commit them to the database

<br />

---

<br />

### 5. Run flask shell and query Production to check seeds

<br />

---

<br />

### 6. Create a `/longest-movies` route to retrieve the longest movie
#### 6a. Import `jsonify` and `make_response`
#### 6b. Use the `route()` decorator
#### 6c. Query for the longest movie
#### 6d. Jsonify and return the response

<br />

---

<br />

### 7. Create a dynamic route `/productions/<string:title>` that searches for all matching records
#### 7a. Use the `route()` decorator
#### 7b. Create a function `def production()` that filters through all Production records and returns the appropriate one
#### 7c. Return the result as json

<br />


### 8. Create a route `/all-productions` to see all productions
#### 8a. Use `serializerMixin` to convert to dictionaries
#### 8b. Use serializer rules to remove `created_at` and `updated_at`