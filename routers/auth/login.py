from flask import Blueprint, request

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
def auth():
    return 'login'

@login_blueprint.route('/login', methods=['POST'])
def login():
    req = request.get_json()

    nome = req['name']
    idade = req['year']
    cargo = req['cargo']

    return [nome, idade, cargo]

