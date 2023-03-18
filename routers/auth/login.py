from flask import Blueprint, request
from . import resister_user, login_user

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
def auth():
    return 'login'

@login_blueprint.route('/login', methods=['POST'])
def login():
    req = request.get_json()

    try:
        password = req['password']
        email = req['email']

        respose = login_user(password, email)
    except KeyError as err:
        return { "Error": f"KeyError: {err}" }

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
        return { "Error": f"KeyError: {err}" }

    return response

@login_blueprint.route('/edit', methods=['PUT'])
def edit():
    req = request.get_json()

    


