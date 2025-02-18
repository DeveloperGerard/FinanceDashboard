from flask import Blueprint, render_template,redirect,request,flash,url_for
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
                                       
@user.route("/home")
@login_required
def home():
    summary = get_financial_summary(current_user.id)  # Obtener el resumen financiero
    user = User.query.get(current_user.id)  # Obtener el usuario con su ID
    print(current_user.username)  # Imprimir el nombre de usuario en la consola
    return render_template("index.html", user=user, summary=summary)  # Pasar datos a la plantilla

@user.route("/cerrar_sesion")
@login_required
def cerrar_sesion():
    logout_user()
    flash('Has cerrado sesión exitosamente.', 'success')
    return redirect(url_for('user.index'))

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