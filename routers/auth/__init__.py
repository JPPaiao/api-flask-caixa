import MySQLdb

def tratament_error(username=None, password=None, email=None, number=None, list_filds=None):
    filds = [username, password, email, number]

    for a in filds:
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
    if list_filds != None:
        for a in list_filds:
            if ['username'] == list(a) and type(a['username']) != str or ['username'] == list(a) and a['username'] == '' or ['username'] == list(a) and a['username'] == None:
                return {
                    "resposta": True,
                    "Error": f"{TypeError('Tipo do campo usuário inválido')}"
                }
            elif ['password'] == list(a) and type(a['password']) != str or ['password'] == list(a) and a['password'] == '' or ['password'] == list(a) and a['password'] == None:
                return {
                    "resposta": True,
                    "Error": f"{TypeError('Tipo do campo password inválido')}"
                }
            elif ['email'] == list(a) and type(a['email']) != str or ['email'] == list(a) and a['email'] == '' or ['email'] == list(a) and a['email'] == None:
                return {
                    "resposta": True,
                    "Error": f"{TypeError('Tipo do campo email inválido')}"
                }
            elif ['number'] == list(a) and type(a['number']) != int or ['number'] == list(a) and a['number'] == '' or ['number'] == list(a) and a['number'] == None:
                return {
                    "resposta": True,
                    "Error": f"{TypeError('Tipo do campo number inválido')}"
                }

    return { "resposta": False }

def validate_users(id, password):
    db = db_connect()
    cursor = db.cursor()

    try:
        cursor.execute(f'''
            SELECT password FROM users WHERE id='{id}'
        ''')
        db.commit()

        rows = list(cursor.fetchmany())
        for row in rows:
            user_password = row[0]

        if rows == []:
            return {
                "resposta": True,
                "Error": "Usuário não encontrado"
            }
        elif password != user_password:
            return {
                "resposta": True,
                "Error": "Senha inválida"
            }
        else:
            return {
                "resposta": False
            }

    except Exception as err:
        return { "Error": f"Error: {err}" }
    finally:
        cursor.close()
        db.close()

def db_connect():
    db = MySQLdb.connect(host='localhost', user='root', password='', database='db_python')
    return db


def query_update(id, values):
    list_filds = []
    for value in values:
        if "username" in list(value):
            list_filds.append(f"name='{value['username']}',")
        elif "password" in list(value):
            list_filds.append(f"password='{value['password']}',")
        elif "email" in list(value):
            list_filds.append(f"email='{value['email']}',")
        elif "number" in list(value):
            list_filds.append(f"number='{value['number']}'")

    join_filds = [" ".join(list_filds)]

    query = f'''
         UPDATE users SET {join_filds[0]} WHERE id='{id}'
     '''

    return query

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
        validate = tratament_error(username=username, password=password, email=email, number=number)

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

def dic_user(list):
    new_list = list[0]
    return {
        "id": new_list[0],
        "name": new_list[1],
        "password": new_list[2],
        "email": new_list[3],
        "number": new_list[4]
    }

def login_user(password, email):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate = tratament_error(password=password, email=email)

        if validate['resposta']:
            return { "Error": validate['Error'] }
        else:
            cursor.execute(f'''
                SELECT * FROM users WHERE password = '{password}' AND email = '{email}';
            ''')
            user_found = dic_user(list(cursor.fetchall()))
            db.commit()

            if user_found == ():
                return { "Error": "E-mail ou senha inválidos!!" }
            else:
                return {
                    "user": user_found,
                    "login": True
                }
    except ValueError as err:
        return { 'Error': f'ValueError: {err}!' }
    finally:
        cursor.close()
        db.close()

def update_user(id, password, values):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate_user = validate_users(id, password)
        validate_filds = tratament_error(list_filds=values)

        if validate_user['resposta']:
            return { "Error": validate_user["Error"] }
        elif validate_filds['resposta']:
            return { "Error": validate_filds["Error"] }
        else:
            query = query_update(id=id, values=values)
            cursor.execute(query)
            db.commit()

            return {
                "Sucess": "Alterações feitas com sucesso"
            }
    except Exception as err:
        return { "Error": f"Error: {err}" }
    finally:
        cursor.close()
        db.close()

def delete_user(id, password):
    db = db_connect()
    cursor = db.cursor()

    try:
        validate = validate_users(id, password)

        if validate['resposta']:
            return { "Error": validate['Error'] }
        else:
            cursor.execute(f'''
                DELETE FROM users WHERE id='{id}'
            ''')
            db.commit()

            return {
                "Sucess": "Usuario deletado com sucesso"
            }

    except Exception as err:
        return { 'Error': f'Error: {err}' }
    finally:
        cursor.close()
        db.close()