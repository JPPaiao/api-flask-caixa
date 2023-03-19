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
                elif a == number and type(a) != int:
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

def users_activate():
    db = db_connect()
    cursor = db.cursor()

    try:
        cursor.execute(f'''
            SELECT name, email, number FROM users;
        ''')
        users = cursor.fetchall()
        db.commit()

        return {
            "Users": users
        }
    except Exception as err:
        return { "Error": f"Error: {err}" }
    finally:
        cursor.close()
        db.close()

def user(id):
    db = db_connect()
    cursor = db.cursor()

    try:
        cursor.execute(f'''
            SELECT name, email, number FROM users WHERE id='{id}';
        ''')
        user_active = cursor.fetchall()
        db.commit()

        return {
            "User": user_active,
        }
    except Exception as err:
        return { "Error": f"Error: {err}" }
    finally:
        cursor.close()
        db.close()

def resister_user(username, password, email, number):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate = tratament_err(username=username, password=password, email=email, number=number)

        if validate["resposta"]:
            return { "Error": validate["Error"] }
        else:
            cursor.execute('INSERT INTO users VALUES (NULL, %s, %s, %s, %s)', (username, password, email, number))
            db.commit()

            return {
                'Sucess': f'Usuário {username} adicionado com sucesso!'
            }
    except ValueError as err:
        return { 'Error': f'ValueError: {err}!' }
    finally:
        cursor.close()
        db.close()

def login_user(password, email):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate = tratament_err(password=password, email=email)

        if validate['resposta']:
            return { "Error": validate['Error'] }
        else:
            cursor.execute(f'''
                SELECT * FROM users WHERE password = '{password}' AND email = '{email}';
            ''')
            user_encontrado = cursor.fetchall()
            db.commit()

            if user_encontrado == ():
                return { "Error": "E-mail ou senha inválidos!!" }
            else:
                return {
                    "User": user_encontrado,
                    "login": True
                }
    except ValueError as err:
        return { 'Error': f'ValueError: {err}!' }
    finally:
        cursor.close()
        db.close()

def update_user(username, password, email, number, id):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate = tratament_err(username=username, password=password, email=email, number=number)

        if validate['resposta']:
            return { "Error": validate['Error'] }
        else:
            cursor.execute(f'''
                UPDATE users SET name='{username}', password='{password}', email='{email}', number='{number}' WHERE id='{id}'
            ''')

            db.commit()

            return {
                "Sucess": "Alterações feitas com sucesso"
            }
    except Exception as err:
        return { 'Error': f'Error: {err}'}
    finally:
        cursor.close()
        db.close()

def delete_user(id):
    db = db_connect()
    cursor = db.cursor()

    try:
        cursor.execute(f''' SELECT name, id FROM users WHERE id='{id}' ''')
        db.commit()

        if cursor.fetchall() == ():
            cursor.execute(f'''
                DELETE FROM users WHERE id='{id}'
            ''')
            db.commit()

            return {
                "Sucess": "Usuario deletado com sucesso"
            }
        else:
            return { "Error": "Usuario não encontrado" }
    except Exception as err:
        return { 'Error': f'Error: {err}' }
    finally:
        cursor.close()
        db.close()