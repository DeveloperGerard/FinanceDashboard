"""
Visualizacion de datos
"""

from flask import Blueprint, render_template
from flask_login import login_required ,current_user
from app.controllers.resumen import get_financial_summary
from app.models.importaciones import Income,Service,User,Account,Loan,Loan_payment,Service_payment,Scheduled_income
from app.forms.importaciones import FormularioCrearCuenta,FormularioCrearServicio,FormularioCrearIngreso,FormularioCrearPrestamos,FormularioCrearIngresoProgamado
from ..extra_functions.email_decorator import email_validation
auth= Blueprint('auth', __name__) 

@auth.route("/home")
@login_required
@email_validation
def home():
    summary = get_financial_summary(current_user.id)  # Obtener el resumen financiero
    user = User().get_by_id(current_user.id)
    return render_template("auth/index.html",user=user,summary=summary)

@auth.route("/vercuentas")
@login_required
@email_validation
def accounts():
    form = FormularioCrearCuenta()
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("auth/vercuentas.html",accounts=accounts,form=form)



@auth.route("/veringresos")
@login_required
@email_validation
def incomes():
    form = FormularioCrearIngreso()
    accounts = Account().get_all_by_userid(current_user.id)
    incomes = Income().get_all_by_userid(current_user.id)
    return render_template("auth/veringresos.html",incomes=incomes,form=form,accounts=accounts)


@auth.route("/veringresosprogramados")
@login_required
@email_validation
def scheduled_incomes():
    form = FormularioCrearIngresoProgamado()
    incomes = Scheduled_income().get_all_by_userid(current_user.id)
    return render_template("auth/veringresosprogramados.html",incomes=incomes,form=form)


@auth.route("/verservicios")
@login_required
@email_validation
def services():
    form = FormularioCrearServicio()
    services = Service().get_all_by_userid(current_user.id)
    accounts = Account().get_all_by_userid(current_user.id)
    service_amount_all = Service().get_full_amount(current_user.id)
    return render_template("auth/verservicios.html",services=services,service_amount_all=service_amount_all,form=form,accounts=accounts)

@auth.route("/verprestamos")
@login_required
@email_validation
def loans():
    accounts = Account().get_all_by_userid(current_user.id)
    form = FormularioCrearPrestamos()
    loans = Loan().get_all_by_userid(current_user.id)
    return  render_template("auth/verprestamos.html",loans=loans,form=form,accounts=accounts)



@auth.route("/resumefinanciero")
@login_required
@email_validation
def resumen_financiero():
    #resumen prestamos
    loan_summary = Loan().get_loan_summary(current_user.id)

    accounts       = Account().get_all_by_userid(current_user.id)
    #resumen pagos prestamos
    loans          = Loan().get_all_by_userid(current_user.id)
    loans_payments = Loan_payment().get_all_by_userid_forsummary(current_user.id)

    #resumen pagos servicios
    services          = Service().get_all_by_userid(current_user.id)
    services_payments = Service_payment().get_all_by_userid_forsummary(current_user.id)

    #obtengo todas los prestamos y servicios divididos en cuentas
    account_loans = Loan().get_all_for_account(current_user.id,accounts)
    account_services = Service().get_all_for_account(current_user.id,accounts)

    #remplazo los servicios y prestamos por sus pagos
    price_service_accounts = Service_payment().get_all_amount_for_account(current_user.id,account_services)
    price_service_loans = Loan_payment().get_all_amount_for_account(current_user.id,account_loans)
    
    #resumen mensual
    loan_month_summary = Loan().get_all_amount_payment(current_user.id)
    service_month_summary = Service().get_all_amount_payment(current_user.id)

    return  render_template("auth/verresumen.html",loan_summary=loan_summary,loans=loans,loans_payments=loans_payments,
                            accounts=accounts,services=services,
                            services_payments=services_payments,
                            pres=price_service_accounts,prep=price_service_loans
                            ,sum=sum,loan_ms=loan_month_summary,service_ms=service_month_summary)
