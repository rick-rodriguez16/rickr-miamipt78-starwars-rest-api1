
import click
from api.models import db, User, Person, Planet

"""
In this file, you can add as many commands as you want using the @app.cli.command decorator
Flask commands are usefull to run cronjobs or tasks outside of the API but sill in integration 
with youy database, for example: Import the price of bitcoin every night as 12am
"""
def setup_commands(app):
    
    """ 
    This is an example command "insert-test-users" that you can run from the command line
    by typing: $ flask insert-test-users 5
    Note: 5 is the number of users to add
    """
    @app.cli.command("insert-test-users") # name of our command
    # @click.argument("count") # argument of out command
    def insert_test_users():
        
        user_list = ['johnsmith123', 'sammysmith456', 'mustangsally789']

        print("Creating test users")
        for x in range(0, len(user_list)):
            user = User()
            user.username = user_list[x]
            db.session.add(user)
            db.session.commit()
            print("User: ", user.username, " created.")

        print("All test users created")




    @app.cli.command("create-people")
    def insert_test_people():
        
        person_name_list = ['Luke Skywalker', 'Darth Vader', 'C-3PO', 'Leah Organa', 'Obiwan Kenobi']
        person_hair_color = ['blonde', 'none', 'none', 'black', 'white']

        print("Creating test people")
        for x in range(0, len(person_name_list)):
            person = Person()
            person.name = person_name_list[x]
            person.hair_color = person_hair_color[x]
            db.session.add(person)
            db.session.commit()
            print("Person: ", person.name, " created.")

        print("All test people created")


    @app.cli.command("create-planets")
    def insert_test_planets():
        # you can create your fake planets SQL code here
        pass
