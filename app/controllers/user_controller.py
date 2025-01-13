from ..models.user import  User
from app import db

class UserController:
    @staticmethod
    def create_user(username,email,password):
        usuario = User()
        usuario.username = username
        usuario.email = email
        usuario.set_password(password)
        usuario.balance = 0
        db.session.add(usuario)
        db.session.commit()
        return usuario
    
    @staticmethod
    def delete_user(usuario:object):
        db.session.delete(usuario)
        db.session.commit()
        return usuario
    
    @staticmethod
    def update_user(usuario:object):
        db.session.add(usuario)
        db.session.commit()

        
