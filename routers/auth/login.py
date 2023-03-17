from flask import Blueprint, request
from . import resister_user

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
def auth():
    return 'login'

@login_blueprint.route('/login', methods=['POST'])
def login():
    req = request.get_json()

    nome = str(req['nome'])
    senha = int(req['senha'])
    email = str(req['email'])

    # try:
    #     cursor = db.cursor()
    #     cursor.execute(f'''SELECT nome FROM users WHERE nome = '{nome}';''')
    #     user_encontrado = list(cursor.fetchall())
    #     db.commit()
    #     cursor.close()

    #     if user_encontrado != []:
    #         return {
    #             "User": user_encontrado,
    #             "login": True
    #         }
    # except:
    return f'Erro: Usuario {nome} não encontrado'


@login_blueprint.route('/register', methods=['POST'])
def register():
    req = request.get_json()

    name = req['name']
    password = req['password']
    email = req['email']
    number = req['number']

    response = resister_user(name, password, email, number)

    return response
