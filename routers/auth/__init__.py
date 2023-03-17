import MySQLdb

def tratament_err(*args):
    arg = list(args)
    try:
        for a in arg:
            if a == '':
                return {
                    "resposta": True,
                    "Error": f"{Exception('Valor vazio!')}"
                }
    except:
        return {
            "resposta": True,
            "Error": f"{Exception('Houve um erro')}"
        }
    else:
        return {
            "resposta": False,
            "Error": "Sem error"
        }

def db_connect():
    db = MySQLdb.connect(host='localhost', user='root', password='', database='db_python')
    return db

def resister_user(username, password, email, number):
    db = db_connect()
    cursor = db.cursor()

    try:
        tratamento = tratament_err(str(username), int(password), str(email), int(number))
        if tratamento["resposta"]:
            return { "Eroor": tratamento["Error"] }
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', (username, password, email, number))
            db.commit()
            cursor.close()

            return { 'Sucess': f'Usuario {username} adicionado com sucesso!' }
    except ValueError as err:
        return { 'Error': f'{err}!' }

def login(username, password, email):
    db = db_connect()
    cursor = db.cursor()

    try:
        cursor.execute(f'''SELECT nome FROM users WHERE nome = '{username}';''')
        user_encontrado = list(cursor.fetchall())
        db.commit()
        cursor.close()

    except Exception as err:
        return { 'Error': f'Error: {err}!' }

    if user_encontrado != []:
        return {
            "User": user_encontrado,
            "login": True
        }
