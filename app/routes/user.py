"""
Visualizacion de datos
"""

from flask import Blueprint, render_template,redirect
from flask_login import login_required ,current_user
from app.models.importaciones import Income,Service,User,Account,Loan
from ..funciones.email_decorator import email_validation
user= Blueprint('user', __name__) 

@user.route('/') 
@user.route('/index') 
def index(): 
    if current_user.is_authenticated:
        if current_user.email_conf is False:
            print("Xddd")
            return render_template("public/confirmation.html")
        else:
            print("Xdddassaasas")
            return redirect('/home')
    else:
        return redirect("/iniciar")
                                       
@login_required
@email_validation
@user.route("/home")
def saludo():
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("user/prueba.html",user=user)

@login_required 
@email_validation
@user.route("/vercuentas")
def ver_cuentas():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("user/vercuentas.html",accounts=accounts)


@login_required 
@email_validation
@user.route("/veringresos")
def ver_ingresos():
    incomes = Income().get_all_by_userid(current_user.id)
    return render_template("user/veringresos.html",incomes=incomes)

@login_required
@email_validation
@user.route("/verservicios")
def ver_servicios():
    services = Service().get_all_by_userid(current_user.id)
    return render_template("user/verservicios.html",services=services)

@login_required
@email_validation
@user.route("/verprestamos")
def ver_prestamos():
    loans = Loan().get_all_by_userid(current_user.id)
    return  render_template("user/verprestamos.html",loans=loans)


@login_required
@email_validation
@user.route("/resumefinanciero")
def resumen_financiero():
    #resumen prestamos
    loan_summ = Loan().get_loan_summary(current_user.id)
    return  render_template("user/verresumen.html",loan_summ=loan_summ)