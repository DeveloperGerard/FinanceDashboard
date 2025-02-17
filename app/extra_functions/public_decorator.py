from flask_login import current_user
from flask import redirect
from ..models.importaciones import User

def no_enter(func):
    """
    Decorador para evitar que un `usuario registrado` acceda a algunas rutas publicas.
    """
    def wrap(*args,**kwargs):
        try:
            user = User().get_by_id(current_user.id)
            if user:
                return redirect("/index")
        except:
            return func(*args,**kwargs)
    wrap.__name__ = func.__name__
    return wrap