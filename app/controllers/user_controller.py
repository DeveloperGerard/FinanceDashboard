from ..models.user import  User
from app import db

class ControladorUsuarios:
    @staticmethod
    def crear_usuario(nombre,correo,clave):
        usuario = User()
        usuario.username = nombre
        usuario.email = correo 
        usuario.set_password(clave)
        usuario.balance = 0
        db.session.add(usuario)
        db.session.commit()
        return usuario

        
