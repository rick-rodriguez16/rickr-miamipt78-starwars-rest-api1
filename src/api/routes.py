"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Person, Planet
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/users', methods=['GET'])
def get_users():

    # query the database to get all the starwars characters
    all_users = User.query.all()

    # take into consideration that there may be None records in the table
    if all_users is None:
        return jsonify('Sorry! No users found!'), 404
    else:
        all_users = list(map(lambda x: x.serialize(), all_users))
        return jsonify(all_users), 200


@api.route('/users/<int:user_id>/favorites', methods=['GET'])
def get_user_favorites(user_id):

    current_user = db.session.get(User, user_id)

    if current_user is None:
        raise APIException('Sorry. User not found', status_code=404)
    
    # need to create the logic to retrieve all the users favorite people
    all_people = [each_person.serialize() for each_person in current_user.favorite_people]

    # need to create the logic to get the users favorite planets
    # you write that code

    response = {
        "message": f'User {current_user.username}\'s list of favorite people',
        "data": {
            "favorite_people": all_people,
            "favorite_planets": all_planets,
        }
    }
    
    return jsonify(response), 200



@api.route('/people', methods=['GET'])
def get_people():

    # query the database to get all the starwars characters
    all_people = Person.query.all()

    # take into consideration that there may be None records in the table
    if all_people is None:
        return jsonify('Sorry! No Star Wars characters found!'), 404
    else:
        all_people = list(map(lambda x: x.serialize(), all_people))
        return jsonify(all_people), 200


@api.route('/people/<int:person_id>', methods=['GET'])
def get_single_person(person_id):

    # query the database to get a SPECIFIC starwars character by id
    single_person = db.session.get(Person, person_id)

    if single_person is None:
        raise APIException(f'Person ID {person_id} was not found!', status_code=404)

    single_person = single_person.serialize()
    return jsonify(single_person), 200





@api.route('/favorite/people/<int:person_id>', methods=['POST'])
def add_favorite_person(person_id):
    # we need 2 things: 
    #   user.id (located in the body of the request) 
    #   person.id (located in the endpoint above)

    user = request.get_json()

    #obtain the User in the database
    user = db.session.get(User, user["user_id"])
    #obtain the Person in the database
    person = db.session.get(Person, person_id)

    # before appending user and person, check that user and person are not None
    # if they are, raise an APIException


    user.favorite_people.append(person)
    db.session.commit()
    return jsonify(f'User {user.username} has added {person.name} to their favorites.'), 200







@api.route('/favorite/people/<int:person_id>', methods=['DELETE'])
def remove_favorite_person(person_id):
    pass





@api.route('/planet', methods=['GET'])
def get_planets():
    pass


@api.route('/planet/<int:planet_id>', methods=['GET'])
def get_single_planet(planet_id):
    pass


@api.route('/favorite/planet/<int:planet_id>', methods=['POST'])
def add_favorite_planet(planet_id):
    pass


@api.route('/favorite/planet/<int:planet_id>', methods=['DELETE'])
def delete_favorite_planet(planet_id):
    pass

