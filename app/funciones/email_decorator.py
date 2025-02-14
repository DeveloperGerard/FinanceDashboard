"""
    Decorador para restringir acceso a rutas a solo usuarios con email confirmado
"""
from flask_login import current_user
from flask import render_template

def email_validation(func):
    def wrap(*args,**kwargs):
        if current_user.email_conf is False:
            return render_template("public/confirmation.html")
        return func(*args,**kwargs)
    wrap.__name__ = func.__name__
    return wrap


