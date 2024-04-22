---

title: 'modeling relationships'

---

# Modeling Relationships in Flask-SQLAlchemy

---

## What We'll Be Doing

- Modeling a one-to-many and many-to-many relationship in Flask-SQLAlchemy
- Using Flask to query those relationships

---

## Single Source of Truth

- AVOID REDUNDANCY
- avoid not updating values in a consistent manner

---

## One-to-Many AKA Belongs-to

<img src="https://curriculum-content.s3.amazonaws.com/7159/python-p4-v2-flask-sqlalchemy/one_many_owning.png" />

```python
#class 'Review'
class Review:
employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
employee = db.relationship('Employee', back_populates="reviews")

#class Employee
class Employee: 
reviews = db.relationship('Review', back_populates="employee")
```

<aside class="notes">

- see drawio
- this is where we add a foreign key column to the Model to store the relationship...don't forget to migrate!
- the relationship stored is the employee associated with the current review
- in the ORM we have to use back_populates to create a reciprocal relationship
- this way we can get a list of reviews for one employee
</aside>

---

## Many-to-Many AKA Has-many-through

<img src="https://curriculum-content.s3.amazonaws.com/7159/python-p4-v2-flask-sqlalchemy/employee_meetings_fk.png" />

<aside class="notes">

- note the intermidary (join) table that holds the foreign keys into unique pairings
</aside>

---

## Association Proxy


Instead of...
```python
meeting = [Meeting.query.filter_by(id=1).first()]
employees = [em.employee for em in meeting.employee_meetings]
```

We can do...
```python
class Meeting:
    employees = association_proxy('employee_meetings', 'employee')
```
<aside class="notes">

- used reach across intermidary model to access related model
- see drawio
</aside>

---

```python

class Employee:
    employee_meetings = db.relationship('EmployeeMeeting', back_populates='employee')
    meetings = association_proxy('employee_meetings', 'meeting')

class EmployeeMeeting:
    employee_id = db.Column(db.Integer, db.ForeignKey('employees.id'))
    meeting_id = db.Column(db.Integer, db.ForeignKey('meetings.id'))

    employee = db.relationship('Employee', back_populates='employee_meetings')
    meeting = db.relationship('Meeting', back_populates='employee_meetings')

class Meeting:
    employee_meetings = db.relationship('EmployeeMeeting', back_populates='meeting')
    employees = association_proxy('employee_meetings', 'employee')
```

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

---

## Max Recursion

- When creating a many-to-many relationship we may reach a max-recursion depth 
- For example with Employee -< EmployeeMeeting >- Meeting if we try to serialize Employee we may get
```python
{
    id: 1,
    name: 'Richard',
    meetings: [
        {
            id: 1,
            topic: 'Where\'s Richard?',
            employees: [
                {
                    id: 1,
                    name: 'Richard',
                    meetings: [
                        {
                            //more meetings...and employees...and meetings...
                        }
                    ]
                }
            ]
        }
    ]
}

```

---

## Max Recursion

- To avoid this we have to specify where to stop by using `serialize_rules(-meetings.employees)`

```python
{
    id: 1,
    name: 'Richard',
    meetings: [
        {
            id: 1,
            topic: 'Where\'s Richard?'
            //no more employees!
        }
    ]
}

```