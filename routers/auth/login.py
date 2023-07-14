from tables_class import User
from connection_db import session

def login_user(data_user):
    try:
        user = session.query(User).filter(User.email == data_user.email).one()

        if user:
            if user.password == data_user.password:
                return {
                    "user": user
                }
            else:
                return {
                    "Error": "Email ou senha não inválido"
                }
        else:
            return {
                "Error": "Erro usuário não encontrado"
            }
    except Exception as e:
        session.rollback()

        return {
            "Error": "Erro ao fazer login"
        } 
    finally:
        session.close()

# ADICIONANDO
def set_user(new_user):
    if new_user:
        try:
            user = User(username=new_user.username, password=new_user.password, email=new_user.email, number=new_user.number)
            session.add(user)
            session.commit()

            return {
                "Success": "Usuario adicionado com sucesso"
            }
        except Exception as e:
            session.rollback()

            return {
                "Error": "Erro usuário não pode ser adicionado"
            } 
        finally:
            session.close()       
    else:
        return {
                "Error": "Erro usuário não pode ser adicionado"
            }

# BUSCANDO
def get_user(email):
    try:
        user = session.query(User).filter(User.email == email)

        if user:
            return {
                "user": user
            }
        else:
            return {
                "Error": "Usuário não encontrado"
            }
    except Exception as e:
        session.rollback()

        return {
            "Error": "Erro ao encontrar usuário"
        } 
    finally:
        session.close()   


def get_users_all():
    users_dict = []

    try:
        users = session.query(User).all()

        for user in users:
            user_dict = {
                'id': user.id,
                'username': user.username,
                'password': user.password,
                'email': user.email,
                'number': user.number
            }

            users_dict.append(user_dict)
    except Exception as e:
        session.rollback()

        return {
            "Error": "Erro ao executar essa operação"
        }
    finally:
        session.close()
    
    return users_dict


# MODIFICANDO
def update_user(id, update):
    try:
        user = session.query(User).filter(User.id == id)

        if user:
            user = user.update(update, synchronize_session='fetch')
            session.commit()
        else:
            return {
                "Error": "Usuário não encontrado"
            }
    except Exception as e:
        session.rollback()

        return {
            "Error": "Erro ao tentar atulizar usuário"
        }
    finally:
        session.close()

# DELETANDO
def delete_user(id):
    try:
        user = session.query(User).get(id)

        if user:
            session.delete(user)
            session.commit()
        else:
            return {
                "Error": "Usuário não encontrado"
            }
    except Exception as e:
        session.rollback()

        return {
            "Error": "Erro ao excluir usuário"
        }
    finally:
        session.close()
