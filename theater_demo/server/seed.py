#!/usr/bin/env python3
from app import app 
from models import Production, db


with app.app_context():

    # create some Production class instances 
    oppenheimer = Production(title="Oppenheimer", year=2023, director="Christopher Nolan", length=180)
    barbie = Production(title="Barbie", year=2023, director="Greta Gerwig", length=114)
    killers_of_the_flower_moon = Production(title="Killers of the Flower Moon", year=2023, director="Martin Scorsese", length=206)
    dune_part_two = Production(title="Dune: Part Two", year=2024, director="Denis Villeneuve", length=155)
    the_marvels = Production(title="The Marvels", year=2024, director="Nia DaCosta", length=105)

    print(oppenheimer.title)
    print(barbie.year)
    # we will save them to the database using SQLAlchemy (aka ORM)

    # db.session.add(oppenheimer)
    # db.session.add(barbie)

    #staging changes
    db.session.add_all([oppenheimer, barbie, killers_of_the_flower_moon, dune_part_two, the_marvels])

    #applying changes to database
    db.session.commit()

    #Production.query.all() => gets all rows as instances of Production 
    #Production.query.filter_by(id=x).all() or .first()
        #.all() => return a list
        #.first() => the first matching row as an instance