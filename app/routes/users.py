from flask import Blueprint, render_template,redirect,request,flash
from flask_login import login_required ,LoginManager,current_user,login_user,logout_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from ..models.user import User

user= Blueprint('user', __name__) 

"""
Aqui van a estar las rutas en las que un usuario registrado
podra visualizar su informacion financiera
"""

@user.route('/') 
@user.route('/index') 
def index(): 
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        return redirect("/iniciar")
                                       
@login_required
@user.route("/home")
def saludo():
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("prueba.html",user=user)
@login_required
@user.route("/cerrar_sesion")
def cerrar():
    logout_user()
    return redirect("/")
