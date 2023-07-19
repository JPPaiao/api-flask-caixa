from flask import Blueprint, request
from .login import login_user, set_user, get_users_all, update_user, delete_user

login_blueprint = Blueprint('endpoints', __name__)

@login_blueprint.route('/users')
def users():
    try:
        response = get_users_all()
    except Exception as err:
        response =  { "Error": f"Error: {err}"}

    return response

@login_blueprint.route('/login', methods=['POST'])
def login():
    req = request.get_json()

    try:
        data_user = {
            "email": req['email'],
            "password": req['password']
        }

        response = login_user(data_user)
    except KeyError as err:
        response = { "Error": f"KeyError: {err}" }

    return response


@login_blueprint.route('/register', methods=['POST'])
def register():
    req = request.get_json()

    try:
        data_user = {
            "username": req['name'],
            "password": req['password'],
            "email": req['email'],
            "number": req['number']
        }

        response = set_user(data_user)
    except KeyError as err:
        response = { "Error": f"KeyError: {err}" }

    return response

@login_blueprint.route('/update/<int:id>', methods=['PUT'])
def update(id):
    response = {}

    if request.method == 'PUT':
        req = request.get_json()

        update = req['update']

        response = update_user(id, update)

    return response

@login_blueprint.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    response = {}

    if request.method == 'DELETE':

        response = delete_user(id)

    return response
