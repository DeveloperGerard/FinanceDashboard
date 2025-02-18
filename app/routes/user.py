from flask import Blueprint, render_template,redirect,request,flash
from flask_login import login_required ,LoginManager,current_user,login_user,logout_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from app.models.importaciones import Income,Service,User,Account,Loan
from app.controllers.resumen import get_financial_summary




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
def home():
    summary = get_financial_summary(current_user.id)
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("index.html",user=user, summary=summary)
@login_required
@user.route("/cerrar_sesion")
def cerrar():
    logout_user()
    return redirect("/")

@login_required 
@user.route("/accounts")
def accounts():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("accounts.html",accounts=accounts)


@login_required 
@user.route("/incomes")
def incomes():
    incomes = Income().get_all_by_userid(current_user.id)
    return render_template("incomes.html",incomes=incomes)

@login_required
@user.route("/services")
def services():
    services = Service().get_all_by_userid(current_user.id)
    return render_template("services.html",services=services)

@login_required
@user.route("/loans")
def loans():
    loans = Loan().get_all_by_userid(current_user.id)
    return  render_template("loan.html",loans=loans)