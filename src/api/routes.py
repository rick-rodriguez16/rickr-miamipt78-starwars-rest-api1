"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
from flask import Flask, request, jsonify, url_for, Blueprint
from api.models import db, User, Person, Favorite_Character
from api.utils import generate_sitemap, APIException
from flask_cors import CORS

api = Blueprint('api', __name__)

# Allow CORS requests to this API
CORS(api)


@api.route('/users', methods=['GET'])
def get_people():

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
    
    # need to create the logic to retrieve all the users favorites
    
    response = {
        'message': f"Here are {current_user.username}'s favorites: ",
        'data': "Need to complete serialization of the user's favorites in this route."
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


# @api.route('/test', methods=['GET'])
# def add_fave_person():

#     user1 = db.session.get(User, 2)
#     print(f'user1 is {user1.id}')
    
#     person1 = db.session.get(Person, 1)
#     print(f'person1 is {person1.id}')


#     return jsonify("Let's see if this worked..."), 200
