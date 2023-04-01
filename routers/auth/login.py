from flask import Blueprint, request
from . import resister_user, login_user, update_user, delete_user, user, users_activate

login_blueprint = Blueprint('login', __name__)

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
        email = req['email']
        password = req['password']

        respose = login_user(password, email)
    except KeyError as err:
        respose = { "Error": f"KeyError: {err}" }

    return respose


@login_blueprint.route('/register', methods=['POST'])
def register():
    req = request.get_json()

    try:
        name = req['name']
        password = req['password']
        email = req['email']
        number = req['number']

        response = resister_user(name, password, email, number)
    except KeyError as err:
        response = { "Error": f"KeyError: {err}" }

    return response

@login_blueprint.route('/update/<int:id>', methods=['PUT'])
def update(id):
    if request.method == 'PUT':
        req = request.get_json()

        password = req['password']
        values = req['values']

        response = update_user(id, password, values)

    return response

@login_blueprint.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        req = request.get_json()
        password = req['password']

        response = delete_user(id, password)

    return response



