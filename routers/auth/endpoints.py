from flask import Blueprint, request
from . import resister_user, update_user, delete_user, user, users_activate
from .login import login_user

login_blueprint = Blueprint('endpoints', __name__)

@login_blueprint.route('/users')
def users():
    try:
        response = users_activate()
    except Exception as err:
        response =  { "Error": f"Error: {err}"}

    return response

@login_blueprint.route('/<int:id>')
def auth(id):
    try:
        response = user(id)
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
        name = req['name']
        password = int(req['password'])
        email = req['email']
        number = int(req['number'])

        response = resister_user(name, password, email, number)
    except KeyError as err:
        response = { "Error": f"KeyError: {err}" }

    return response

@login_blueprint.route('/update/<int:id>', methods=['PUT'])
def update(id):
    response = {}

    if request.method == 'PUT':
        req = request.get_json()

        password = req['password']
        values = req['values']

        response = update_user(id, password, values)

    return response

@login_blueprint.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    response = {}

    if request.method == 'DELETE':
        req = request.get_json()
        password = req['password']

        response = delete_user(id, password)

    return response
