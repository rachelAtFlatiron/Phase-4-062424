from app import app
from models import db, Production, Role, Actor
from faker import Faker

with app.app_context():
    Production.query.delete()
    Role.query.delete()
    Actor.query.delete()
    inception = Production(title='Inception',
                         genre='Sci-Fi',
                         length=148,
                         image='https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxNF5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_FMjpg_UX1000_.jpg',
                         language='English',
                         director='Christopher Nolan',
                         description='A thief who enters the dreams of others to steal their secrets',
                         composer='Hans Zimmer',
                         year=2010)
    
    dune = Production(title='Dune',
                            genre='Sci-Fi',
                            length=155,
                            image='https://m.media-amazon.com/images/M/MV5BMDQ0NjgyN2YtNWViNS00YjA3LTkxNDktYzFkZTExZGMxZDkxXkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg',
                            language='English',
                            director='Denis Villeneuve',
                            description='Feature adaptation of Frank Herbert\'s science fiction novel, about the son of a noble family entrusted with the protection of the most valuable asset and most vital element in the galaxy.',
                            composer='Hans Zimmer',
                            year=2021)

    dune_two = Production(title='Dune 2',
                            genre='Sci-Fi',
                            length=0,  # You can update this once more information about the movie is available
                            image='https://m.media-amazon.com/images/M/MV5BN2QyZGU4ZDctOWMzMy00NTc5LThlOGQtODhmNDI1NmY5YzAwXkEyXkFqcGdeQXVyMDM2NDM2MQ@@._V1_FMjpg_UX1000_.jpg',  # Assuming same image for now
                            language='English',
                            director='To be announced',
                            description='Upcoming sequel to the film adaptation of Frank Herbert\'s science fiction novel "Dune".',
                            composer='To be announced',
                            year=2023)  # Hypothetical release year

    barbie = Production(title='The Barbie Movie',
                            genre='Animation',
                            length=0,  # Length information not available
                            image='https://m.media-amazon.com/images/M/MV5BNjU3N2QxNzYtMjk1NC00MTc4LTk1NTQtMmUxNTljM2I0NDA5XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_.jpg',  # Placeholder image
                            language='English',
                            director='To be announced',
                            description='Upcoming animated movie based on the popular Barbie doll franchise.',
                            composer='To be announced',
                            year=2023)  # Hypothetical release year

    dont_look = Production(title="Don't Look Up",
                            genre='Comedy',
                            length=145,
                            image='https://m.media-amazon.com/images/M/MV5BZjcwZjY3NjAtNzkxZS00NmFjLTg1OGYtODJmMThhY2UwMTc5XkEyXkFqcGdeQXVyODE5NzE3OTE@._V1_FMjpg_UX1000_.jpg',
                            language='English',
                            director='Adam McKay',
                            description='Two low-level astronomers must go on a giant media tour to warn mankind of an approaching comet that will destroy planet Earth.',
                            composer='Nicholas Britell',
                            year=2021)
    
    hollywood = Production(title='Once Upon a Time in Hollywood',
                            genre='Comedy',
                            length=161,
                            image='https://m.media-amazon.com/images/M/MV5BOTg4ZTNkZmUtMzNlZi00YmFjLTk1MmUtNWQwNTM0YjcyNTNkXkEyXkFqcGdeQXVyNjg2NjQwMDQ@._V1_FMjpg_UX1000_.jpg',
                            language='English',
                            director='Quentin Tarantino',
                            description='A faded television actor and his stunt double strive to achieve fame and success in the final years of Hollywood\'s Golden Age in 1969 Los Angeles.',
                            composer='Various Artists',
                            year=2019)

    db.session.add_all([inception, dune, dune_two, barbie, dont_look, hollywood])
# ------------------------------------------------------

    zendaya = Actor(name='Zendaya', image='https://upload.wikimedia.org/wikipedia/commons/thumb/2/28/Zendaya_-_2019_by_Glenn_Francis.jpg/800px-Zendaya_-_2019_by_Glenn_Francis.jpg', age=25, country='United States')
    timmy = Actor(name='Timothée Chalamet', image='https://cdn.britannica.com/36/231936-050-63D849FB/Timothee-Chalamet-2021.jpg', age=26, country='United States')
    leo = Actor(name='Leonardo DiCaprio', image='https://m.media-amazon.com/images/M/MV5BMjI0MTg3MzI0M15BMl5BanBnXkFtZTcwMzQyODU2Mw@@._V1_FMjpg_UX1000_.jpg', age=47, country='United States')
    gosling = Actor(name='Ryan Gosling', image='https://m.media-amazon.com/images/M/MV5BMTQzMjkwNTQ2OF5BMl5BanBnXkFtZTgwNTQ4MTQ4MTE@._V1_.jpg', age=41, country='Canada')
    margot = Actor(name='Margot Robbie', image='https://cdn.britannica.com/32/201632-050-66971649/actress-Margot-Robbie-Australian-2018.jpg', age=31, country='Australia')

    db.session.add_all([zendaya, timmy, leo, gosling, margot])
    # -----------------------------------------------------------------

    zendaya_dune_role = Role(production=dune, actor=zendaya, role_name='Chani')
    zendaya_dune2_role = Role(production=dune_two, actor=zendaya, role_name='Chani')

    chalamet_dune_role = Role(production=dune, actor=timmy, role_name='Paul Atreides')
    chalamet_dune2_role = Role(production=dune_two, actor=timmy, role_name='Paul Atreides')
    chalamet_dont_look = Role(production=dont_look, actor=timmy, role_name='Yule')

    # Role for Leonardo DiCaprio in Inception
    dicaprio_inception_role = Role(production=inception, actor=leo, role_name='Cobb')

    # Role for Leonardo DiCaprio in Don't Look Up
    dicaprio_dont_look_up_role = Role(production=dont_look, actor=leo, role_name='Dr. Randall Mindy')

    dicaprio_hollywood = Role(production=hollywood, actor=leo, role_name="Rick Dalton")

    # Assuming you have the productions 'The Barbie Movie' and 'Once Upon a Time in Hollywood' already defined

    # Role for Margot Robbie in The Barbie Movie
    robbie_barbie_role = Role(production=barbie, actor=margot, role_name='Barbie')

    # Role for Margot Robbie in Once Upon a Time in Hollywood
    robbie_once_upon_role = Role(production=hollywood, actor=margot, role_name='Sharon Tate')

    gosling_barbie_role = Role(production=barbie, actor=gosling, role_name='Ken')

    db.session.add_all([zendaya_dune2_role, zendaya_dune_role, chalamet_dune2_role, chalamet_dont_look, chalamet_dune_role, dicaprio_dont_look_up_role, dicaprio_hollywood, dicaprio_inception_role, robbie_barbie_role, robbie_once_upon_role, gosling_barbie_role])

    db.session.commit()