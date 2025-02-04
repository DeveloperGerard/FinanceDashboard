from flask import Blueprint, render_template,redirect,request,flash
from flask_login import login_required ,LoginManager,current_user,login_user,logout_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from app.models.importaciones import Income,Service,User,Account,Loan
from ..funciones.email_decorator import email_validation
user= Blueprint('user', __name__) 

"""
Aqui van a estar las rutas en las que un usuario registrado
podra visualizar su informacion financiera
"""

@user.route('/') 
@user.route('/index') 
def index(): 
    if current_user.is_authenticated:
        if current_user.email_conf:
            return redirect('/home')
        else:
            return render_template("public/confirmation.html")
    else:
        return redirect("/iniciar")
                                       
@login_required
@user.route("/home")
def saludo():
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("user/prueba.html",user=user)
@login_required
@user.route("/cerrar_sesion")
def cerrar():
    logout_user()
    return redirect("/")

@login_required 
@user.route("/vercuentas")
@email_validation
def ver_cuentas():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("user/vercuentas.html",accounts=accounts)


@login_required 
@user.route("/veringresos")
def ver_ingresos():
    incomes = Income().get_all_by_userid(current_user.id)
    return render_template("user/veringresos.html",incomes=incomes)

@login_required
@user.route("/verservicios")
def ver_servicios():
    services = Service().get_all_by_userid(current_user.id)
    return render_template("user/verservicios.html",services=services)

@login_required
@user.route("/verprestamos")
def ver_prestamos():
    loans = Loan().get_all_by_userid(current_user.id)
    return  render_template("user/verprestamos.html",loans=loans)