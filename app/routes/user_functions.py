from flask import Blueprint,render_template,redirect,request,flash
from flask_login import current_user,login_required
from app.models.account import Account
from app.forms.form_account import FormularioActualizarCuenta,FormularioCrearCuenta
from app.controllers.account_controller import AccountController
user_functions = Blueprint('user_functions',__name__)

"""
Aqui van a estar las rutas relacionadas con las funciones que 
puede realizar el usuario como crear prestamos,servicios,etc.

"""
@login_required
@user_functions.route("/crearcuenta",methods=["GET","POST"])
def crear_cuenta():
    if request.method =="GET":
        form = FormularioCrearCuenta()
        return render_template("user_functions/crear_cuenta.html",form=form)
    if request.method == "POST":
        form = FormularioCrearCuenta()
        if form.validate_on_submit():
            nombre  = form.nombre.data
            tipo    = form.tarjeta.data
            user_id = current_user.id
            AccountController().create_account(nombre,tipo,user_id)
            return redirect("/index")
@login_required 
@user_functions.route("/vercuentas")
def vercuentas():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("user_functions/vercuentas.html",accounts=accounts)