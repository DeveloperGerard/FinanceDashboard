"""
 Funciones extra
"""


#modulos externos
from flask                                import Blueprint,redirect,flash,render_template,jsonify
from flask_login                          import current_user,login_required,logout_user

#modulos propios
from ..extra_functions.token              import confirm_token,genera_token
from ..extra_functions.notification_funct import send_gmail_confirmation
from ..extra_functions.email_decorator    import email_validation
from ..models.importaciones               import User,Account,Income,Loan,Service,Scheduled_income
from ..controllers.importaciones          import UserController
extra_functions = Blueprint("extra_functions",__name__)


@extra_functions.route('/') 
@extra_functions.route('/index') 
def index(): 
    if current_user.is_authenticated:
        if current_user.email_conf is False:
            return render_template("extra_functions/confirmation.html")
        else:    
            return redirect('/home')
    else:
        return redirect("/iniciar")
                                       
@extra_functions.route("/conf_email/<token>")
@login_required
def confirm_email(token):
    if current_user.email_conf:
        return redirect("/index")
    email = confirm_token(token)
    user = User().get_by_id(current_user.id)
    if user.email == email:
        user.email_conf= True
        UserController().update_user(user)
        flash("Cuenta confirmada")
        return redirect("/index")
    else:
        flash("Token invalido")
        #aqui añadir que muestre token vencido
        return "xd"

@extra_functions.route("/reenviartoken")
@login_required
def reenviar_token():
    user  = User().get_by_id(current_user.id)
    token = genera_token(user.email)
    send_gmail_confirmation(token)
    return redirect("https://mail.google.com/")


@extra_functions.route("/cerrar_sesion")
@login_required
@email_validation
def cerrar():
    logout_user()
    return redirect("/")

@extra_functions.route("/informacion_cuenta/<int:id>")
@login_required
@email_validation
def info_cuenta(id):
    account = Account().get_by_id(id)
    account_data = {
        'card':account.card,
        'account_name':account.account_name,
    }
    return jsonify(account_data)

@extra_functions.route("/informacion_ingreso/<int:id>")
@login_required
@email_validation
def info_ingreso(id):
    income = Income().get_by_id(id)
    income_data = {
        'income_name':income.income_name,
        'income_date':income.income_date,
        'description':income.description,
        'category':income.category,
        'amount':income.amount
    }
    return jsonify(income_data)

@extra_functions.route("/informacion_prestamo/<int:id>")
@login_required
@email_validation
def info_prestamo(id):
    loan = Loan().get_by_id(id)
    loan_data = {
        "name":loan.loan_name,
        "holder":loan.holder,
        "price":loan.price,
        "quota":loan.quota,
        "tea":loan.tea,
        "expiration_date":loan.expiration_date
    }
    return jsonify(loan_data)

@extra_functions.route("/informacion_servicio/<int:id>")
@login_required
@email_validation
def info_servicio(id):
    service = Service().get_by_id(id)
    service_data = {
        "name":service.service_name,
        "description":service.description,
        "category":service.category,
        "price":service.price,
        "expiration_date":service.expiration_date
    }
    return jsonify(service_data)

@extra_functions.route("/informacion_ingreso_programado/<int:id>")
@login_required
@email_validation
def info_ingreso_programado(id):
    income = Scheduled_income().get_by_id(id)
    income_data = {
        "name":income.income_name,
        "description":income.description,
        "category":income.category,
        "amount":income.amount,
        "next_income":income.next_income
    }
    return jsonify(income_data)



