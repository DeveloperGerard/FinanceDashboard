"""
Visualizacion de datos
"""

from flask import Blueprint, render_template,redirect
from flask_login import login_required ,current_user
from app.models.importaciones import Income,Service,User,Account,Loan,Loan_payment,Service_payment
from ..extra_functions.email_decorator import email_validation
auth= Blueprint('auth', __name__) 

@auth.route('/') 
@auth.route('/index') 
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
                                       
@auth.route("/home")
@login_required
@email_validation
def saludo():
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("auth/prueba.html",user=user)

@auth.route("/vercuentas")
@login_required
@email_validation
def ver_cuentas():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("auth/vercuentas.html",accounts=accounts)



@auth.route("/veringresos")
@login_required
@email_validation
def ver_ingresos():
    incomes = Income().get_all_by_category(current_user.id)
    print(incomes)
    return render_template("auth/veringresos.html",incomes=incomes)


@auth.route("/verservicios")
@login_required
@email_validation
def ver_servicios():
    services = Service().get_all_by_userid(current_user.id)
    service_amount_all = Service().get_full_amount(current_user.id)
    return render_template("auth/verservicios.html",services=services,service_amount_all=service_amount_all)

@auth.route("/verprestamos")
@login_required
@email_validation
def ver_prestamos():
    loans = Loan().get_all_by_userid(current_user.id)
    print(loans)
    return  render_template("auth/verprestamos.html",loans=loans)



@auth.route("/resumefinanciero")
@login_required
@email_validation
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
    print(cuentas)
    cuentas_2 = Service().get_all_for_account(current_user.id,accounts)
    print(cuentas_2)
    """
    precio_cuenta = Loan_payment().get_all_payment_for_loans(cuentas)
    precio_cuenta2 = Service_payment().get_all_payment_for_services(cuentas_2)"""
    precio_cuenta2 = [[222],[222]]
    precio_cuenta = [[222],[222]]

    #resumen mensual
    prestamos_re = Loan().get_all_amount_payment(current_user.id)
    servicios_re = Service().get_all_amount_payment(current_user.id)

    return  render_template("auth/verresumen.html",loan_summ=loan_summ,loans=loans,loans_payments=loans_payments,accounts=accounts,services=services,
                            services_payments=services_payments,precio_cuenta=precio_cuenta,precio_cuenta2=precio_cuenta2,sum=sum,prestamos_re=prestamos_re,servicios_re=servicios_re)
