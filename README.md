# Modeling Relationships: Deliverables

---

## SWBATs

- [ ] Use Flask-SQLAlchemy to model a many-to-many relationship
- [ ] Use Flask-SQLAlchemy to model a one-to-many relationship
- [ ] Use SQLAlchemy-Serializer to prevent max recursion

---

### 1. Create a `Role` model
#### 1a. Create a one-to-many relationship between `Role` and `Production`
#### 1b. Fetch the route `/productions` to see all the roles associated with each production
#### 1c. Create a `/roles` route to see the other side of the one-to-many relationship

### 2. Create an `Actor` model
#### 2a. Create a one-to-many relationship between `Role` and `Actor`
#### 2b. Fetch the route `/roles` to see all the roles associated with each actor
#### 2c. Create an `/actors` route to see the other side of the one-to-many relationship

### 3. Create many-to-many relationship between `Production` and `Actor` using `association_proxy`
#### 3a. Use `SerializerMixin` to prevent max recursion
#### 3b. Create routes to access all actors and all productions
