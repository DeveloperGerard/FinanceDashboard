from flask import Blueprint,render_template,redirect,request,flash
from flask_login import current_user,login_required
from app.forms.form_income import FormularioCrearIngreso
from app.forms.form_account import FormularioActualizarCuenta,FormularioCrearCuenta
from app.forms.form_service import FormularioCrearServicio
from app.forms.form_loanpayments import FormularioCrearPagoPrestamo
from app.forms.form_loan import FormularioCrearPrestamos
from app.controllers.importaciones import AccountController,IncomeController,UserController,ServiceController,LoanController,LoanPaymentController
from app.models.importaciones import Income,Account,User,Service,Loan
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

@login_required
@user_functions.route("/crearprestamo",methods=["GET","POST"])
def crear_prestamo():
    if request.method == "GET":
        form = FormularioCrearPrestamos()
        accounts = Account().get_all_by_userid(current_user.id)
        return render_template("user_functions/crear_prestamo.html",form=form,accounts=accounts)
    if request.method == "POST":
        form = FormularioCrearPrestamos()
        if form.validate_on_submit():
            nombre   = form.nombre.data
            titular  = form.titular.data 
            precio   = form.precio.data
            cuota    = form.cuota.data
            user_id  = current_user.id
            tea      = form.tea.data
            tea_mora = form.tea_mora.data
            cuenta   = int(request.form.get("cuenta"))
            LoanController().create_loan(nombre,titular,precio,cuota,user_id,cuenta,precio,tea,tea_mora)
            return redirect("/index")
        else:
            return render_template("user_functions/crear_prestamo.html",form=form)
        
"""
    ESTO DA ERROR = Nombre:Montar una biblioteca de manga,Titular=Laios,Precio= 3000000,Cuota=12,Tea=0,Tea_mora=0 Banco fallabela
    Esto no me dio error Nombre=Montar un laboratorio robotico,Titular=Gerard,Precio=5000000,quota=12,tea=0,tea_mora=0,
    user id y el msimo
    ahora provaremos    
"""

@login_required
@user_functions.route("/pagoprestamo",methods=["GET","POST"])
def pago_prestamo():
    if request.method =="GET":
        form = FormularioCrearPagoPrestamo()
        loans = Loan().get_all_by_userid(current_user.id)
        return render_template("user_functions/crear_pago_prestamo.html",form=form,loans=loans)
    if request.method =="POST":
        form = FormularioCrearPagoPrestamo()
        if form.validate_on_submit:
            monto    = form.monto.data
            fecha    = form.fecha.data
            descrip  = form.descripcion.data
            prestamo = int(request.form.get("prestamo"))
            LoanPaymentController().create_loan_payment(monto,fecha,descrip,prestamo)
            prestamo = Loan().get_by_id(prestamo)
            prestamo.reamining_price = prestamo.reamining_price -monto
            LoanController().update_loan(prestamo)
            return redirect("/index")
            

    