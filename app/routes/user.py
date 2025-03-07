from flask import Blueprint, render_template,redirect,request,flash,url_for
from flask_login import login_required ,LoginManager,current_user,login_user,logout_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from app.models.importaciones import Income,Service,User,Account,Loan
from app.controllers.resumen import get_financial_summary
from ..extra_functions.token              import confirm_token,genera_token
from ..extra_functions.notification_funct import send_gmail_confirmation
from ..extra_functions.email_decorator    import email_validation





user= Blueprint('user', __name__) 

"""
Aqui van a estar las rutas en las que un usuario registrado
podra visualizar su informacion financiera
"""

@user.route('/') 
@user.route('/index') 
def index(): 
    if current_user.is_authenticated:
        if current_user.email_conf is False:
            return render_template("extra_functions/confirmation.html")
        else:    
            return redirect('/home')
    else:
        return redirect("/iniciar")
                                       
@user.route("/home")
@login_required
@email_validation
def home():
    incomes = Income.query.filter_by(user_id=current_user.id).all()
    services = Service.query.filter_by(user_id=current_user.id).all()
    loans = Loan.query.filter_by(user_id=current_user.id).all()

    # Construir la lista de movimientos
    movements = []

    for income in incomes:
        movements.append({
            "description": f"Ingreso: {income.income_name}",
            "amount": income.amount
        })

    for service in services:
        movements.append({
            "description": f"Gasto en Servicio: {service.service_name}",
            "amount": -service.price  # Gasto es negativo
        })

    for loan in loans:
        movements.append({
            "description": f"Préstamo: {loan.loan_name}",
            "amount": -loan.remaining_price  # Deuda es negativa
        })
    summary = get_financial_summary(current_user.id)  # Obtener el resumen financiero
    user = User.query.get(current_user.id)  # Obtener el usuario con su ID
    print(current_user.username)  # Imprimir el nombre de usuario en la consola
    return render_template("index.html", user=user, summary=summary, movements=movements)  # Pasar datos a la plantilla

@user.route("/cerrar_sesion")
@login_required
@email_validation
def cerrar():
    logout_user()
    return redirect("/")


@user.route("/accounts")
@login_required
@email_validation
def accounts():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("accounts.html",accounts=accounts)


@user.route("/incomes")
@login_required
@email_validation
def incomes():
    incomes = Income().get_all_by_userid(current_user.id)
    return render_template("incomes.html",incomes=incomes)

@user.route("/services")
@login_required
@email_validation
def services():
    services = Service().get_all_by_userid(current_user.id)
    return render_template("services.html",services=services)

@user.route("/loans")
@login_required
@email_validation
def loans():
    loans = Loan().get_all_by_userid(current_user.id)
    return  render_template("loan.html",loans=loans)