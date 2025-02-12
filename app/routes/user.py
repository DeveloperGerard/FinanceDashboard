"""
Visualizacion de datos
"""

from flask import Blueprint, render_template,redirect
from flask_login import login_required ,current_user
from app.models.importaciones import Income,Service,User,Account,Loan,Loan_payment,Service_payment
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

    accounts       = Account().get_all_by_userid(current_user.id)
    #resumen pagos prestamos
    loans          = Loan().get_all_by_userid(current_user.id)
    loans_payments = Loan_payment().get_all_by_userid(current_user.id)

    #resumen pagos servicios
    services          = Service().get_all_by_userid(current_user.id)
    services_payments = Service_payment().get_all_by_userid(current_user.id)

    #cuentas
    cuentas = Loan().get_all_for_account(current_user.id,accounts)
    precio_cuenta = Loan_payment().get_all_payment_for_loans(current_user.id,cuentas)

    cuentas_2 = Service().get_all_for_account(current_user.id,accounts)
    precio_cuenta2 = Service_payment().get_all_payment_for_loans(current_user.id,cuentas_2)

    #resumen mensual
    prestamos_re = loan_summ["monto_pagado"]
    servicios_re = Service().get_all_amount_payment(current_user.id)

    return  render_template("user/verresumen.html",loan_summ=loan_summ,loans=loans,loans_payments=loans_payments,accounts=accounts,services=services,
                            services_payments=services_payments,precio_cuenta=precio_cuenta,precio_cuenta2=precio_cuenta2,sum=sum,prestamos_re=prestamos_re,servicios_re=servicios_re)

