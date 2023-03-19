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
        password = req['password']
        email = req['email']

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

        if req.get('name'):
            name = req['name']
        if req.get('password'):
            password = req['password']
        if req.get('email'):
            email = req['email']
        if req.get('number'):
            number = req['number']

        if name or password or email or number:
            response = update_user(username=name, password=password, email=email, number=number, id=id)

    return response

@login_blueprint.route('/delete/<int:id>', methods=['DELETE'])
def delete(id):
    if request.method == 'DELETE':
        req = request.get_json()
        password = req['password_delete']

        if password == 3003:
            response = delete_user(id)
        else:
            response = { 'Error': 'Senha inválida' }

    return response



