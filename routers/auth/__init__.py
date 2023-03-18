import MySQLdb

def tratament_err(username=None, password=None, email=None, number=None):
    args = [username, password, email, number]

    try:
        for a in args:
            if a != None:
                if a == username and type(a) != str or a == email and type(a) != str:
                    return {
                        "resposta": True,
                        "Error": f"{TypeError('Tipo errado')}"
                    }
                elif a == password and type(a) != int or a == number and type(a) != int:
                    return {
                        "resposta": True,
                        "Error": f"{TypeError('Tipo errado')}"
                    }
                elif a == "":
                    return {
                        "resposta": True,
                        "Error": f"{ValueError('Valor vazio!')}"
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
        validate = tratament_err(username=username, password=password, email=email, number=number)

        if validate["resposta"]:
            return { "Eroor": validate["Error"] }
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', (username, password, email, number))
            db.commit()
            cursor.close()

            return {
                'Sucess': f'Usuario {username} adicionado com sucesso!'
            }
    except ValueError as err:
        return { 'Error': f'ValueError: {err}!' }

def login_user(password, email):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate = tratament_err(password=password, email=email)

        if validate['resposta']:
            return { "Error": validate['Error'] }
        else:
            cursor.execute(f'''
                SELECT id, name FROM users WHERE password = '{password}' AND email = '{email}';
            ''')
            user_encontrado = cursor.fetchall()
            db.commit()
            cursor.close()
            if user_encontrado == ():
                return { "Error": "E-mail ou senha invalidos!!" }
            else:
                return {
                    "User": user_encontrado,
                    "login": True
                }
    except ValueError as err:
        return { 'Error': f'ValueError: {err}!' }

