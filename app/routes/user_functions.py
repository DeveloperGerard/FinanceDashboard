from flask import Blueprint,render_template,redirect,request,flash
from flask_login import current_user,login_required
from app.forms.form_income import FormularioCrearIngreso
from app.forms.form_account import FormularioActualizarCuenta,FormularioCrearCuenta
from app.forms.form_service import FormularioCrearServicio
from app.controllers.importaciones import AccountController,IncomeController,UserController,ServiceController
from app.models.importaciones import Income,Account,User,Service
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
@user_functions.route("/crearservicio",methods=["GET","POST"])
def crear_servicio():
    if request.method == "GET":
        form = FormularioCrearServicio()
        return render_template("user_functions/crear_servicio.html",form=form)
    if request.method == "POST":
        form = FormularioCrearServicio()
        if form.validate_on_submit():
            nombre      = form.nombre.data
            descripcion = form.descripcion.data
            fecha       = form.fecha.data
            categoria   = form.categoria.data
            precio      = form.precio.data
            user_id     = current_user.id
            ServiceController().create_service(nombre,descripcion,fecha,categoria,user_id,precio,precio)
            return redirect("/index")
