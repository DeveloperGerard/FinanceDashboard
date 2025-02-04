from flask_login import current_user
from flask import redirect,render_template
def email_validation(func):
    def wrap(*args,**kwargs):
        if current_user.email_conf is False:
            return render_template("public/confirmation.html")
        return func(*args,**kwargs)
    return wrap


