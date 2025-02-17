from ..models.user import  User
from app import db

class UserController:
    """
        Controlador de `Usuarios`.

        Permite realizar las funciones basicas(`borrar,actualizar,crear objetos`) del modelo usuarios.
    """

    @staticmethod
    def create_user(username,email,password):
        user = User()
        user.username = username
        user.email = email
        user.set_password(password)
        user.balance = 0
        db.session.add(user)
        db.session.commit()
        return user
    
    @staticmethod
    def delete_user(user:object):
        db.session.delete(user)
        db.session.commit()
        return user
    
    @staticmethod
    def update_user(user:object):
        db.session.add(user)
        db.session.commit()

        
