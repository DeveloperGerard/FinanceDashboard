from flask import Blueprint,render_template,redirect,request,flash
from flask_login import current_user,login_required
"""from app.models.account import Account
from app.models.income import Income"""
from app.forms.form_income import FormularioCrearIngreso
from app.forms.form_account import FormularioActualizarCuenta,FormularioCrearCuenta
from app.controllers.importaciones import AccountController,IncomeController,UserController
from app.models.importaciones import Income,Account,User
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
            tarjeta    = form.tarjeta.data
            user_id = current_user.id
            AccountController().create_account(nombre,tarjeta,user_id)
            return redirect("/index")
@login_required 
@user_functions.route("/vercuentas")
def vercuentas():
    accounts = Account().get_all_by_userid(current_user.id)
    return render_template("user_functions/vercuentas.html",accounts=accounts)



@login_required
@user_functions.route("/crearingreso",methods=["GET","POST"])
def crear_ingreso():
    if request.method =="GET":
        form = FormularioCrearIngreso()
        return render_template("user_functions/crear_ingreso.html",form=form)
    if request.method == "POST":
        form = FormularioCrearIngreso()
        if form.validate_on_submit():
            nombre  = form.nombre.data
            fecha   = form.fecha.data
            user_id = current_user.id
            monto   = form.monto.data
            IncomeController().create_income(nombre,fecha,monto,user_id)
            usuario = User().get_by_id(current_user.id)
            usuario.balance = usuario.balance + monto
            UserController().update_user(usuario)
            return redirect("/index")
@login_required 
@user_functions.route("/veringresos")
def veringresos():
    incomes = Income().get_all_by_userid(current_user.id)
    return render_template("user_functions/veringresos.html",incomes=incomes)