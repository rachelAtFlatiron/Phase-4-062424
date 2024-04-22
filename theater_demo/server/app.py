# handle creating the api and connecting the database 
# and enabling alembic/migrations

# ✅ 1. Navigate to `models.py`

# ✅ 2a. Set Up Imports
# ✅ 2b. Create instance of Flask
# ✅ 2c. Configure the flask app to connect to a database
# ✅ 2d. Enable Flask-Migrate's Alembic by using `Migrate`
# ✅ 2e. Connect the database to the app
# ✅ 3. Migrate the Production model using Flask-Migrate's Alembic

# ✅ 4. Navigate to `seed.rb`

# ✅ 6. Create a path to retrieve the first 5 longest movies
# ✅ 6a. Import jsonify, make_response
# ✅ 6b. Use the `route` decorator
# ✅ 6c. Query for longest movie
# ✅ 6d. Jsonify and return the response


# ✅ 7. Create a dynamic route
# ✅ 7a. Use the route decorator
# ✅ 7b. Create productions() to filter through db

# ✅ 7c. Return result as JSON

# ✅ 8. Create a dynamic route `/productions/<int:id>` that searches for all matching records

# ✅ 9. Create a route `/all-productions` to see all productions
# ✅ 9a. use SerializerMixin's .to_dict() for responses here and everywhere


# Note: If you'd like to run the application as a script instead of using `flask run`, uncomment the line below 
# and run `python app.py`

# if __name__ == '__main__':
#     app.run(port=5555, debug=True)