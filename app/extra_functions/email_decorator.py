from flask_login import current_user
from flask import render_template

def email_validation(func):
    """
        Este decorador restringe el acceso a rutas 
        para que solo los usuarios con `correo confirmado`
        puedan ingresar.
    """
    def wrap(*args,**kwargs):
        if current_user.email_conf is False:
            return render_template("extra_functions/confirmation.html")
        return func(*args,**kwargs)
    wrap.__name__ = func.__name__
    return wrap


