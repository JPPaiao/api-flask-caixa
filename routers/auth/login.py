from flask import Blueprint, request
import MySQLdb

login_blueprint = Blueprint('login', __name__)

@login_blueprint.route('/')
def auth():
    return 'login'

@login_blueprint.route('/login', methods=['POST'])
def login():
    req = request.get_json()

    nome = req['nome']
    senha = req['senha']
    email = req['email']

    db = MySQLdb.connect(host='localhost', user='root', password='', database='db_python')
    cursor = db.cursor()

    cursor.execute('SELECT * FROM users')

    res = cursor.fetchall()
    res_list = list(res)

    print(res_list)
    db.commit()
    cursor.close()

    return { "res": res_list }

@login_blueprint.route('/register', methods=['POST'])
def register():
    req = request.get_json()

    name = req['nome']
    senha = req['senha']
    email = req['email']

    db = MySQLdb.connect(host='localhost', user='root', password='', database='db_python')
    cursor = db.cursor()

    cursor.execute('INSERT INTO users VALUES (NULL, % s, % s, % s)', (name, senha, email, ))
    db.commit()

    print(db.fetchall())

    cursor.close()

    return 'ok'
