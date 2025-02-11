"""
Funciones del usuario

"""

from flask                          import Blueprint,render_template,redirect,request,flash
from flask_login                    import current_user,login_required,logout_user
from app.forms.form_income          import FormularioCrearIngreso
from app.forms.form_account         import FormularioCrearCuenta
from app.forms.form_service         import FormularioCrearServicio
from app.forms.form_loanpayments    import FormularioCrearPagoPrestamo
from app.forms.form_servicepayments import FormularioCrearPagoServicio
from app.forms.form_loan            import FormularioCrearPrestamos
from app.controllers.importaciones  import AccountController,IncomeController,UserController,ServiceController,LoanController,LoanPaymentController,ServicePaymentController
from app.models.importaciones       import Income,Account,User,Service,Loan
from ..funciones.token import confirm_token,genera_token
from ..funciones.notification_funct import send_gmail_confirmation
from ..funciones.email_decorator import email_validation
user_functions = Blueprint('user_functions',__name__)



@login_required
@email_validation
@user_functions.route("/crearcuenta",methods=["GET","POST"])
def crear_cuenta():
    if request.method =="GET":
        form = FormularioCrearCuenta()
        return render_template("user_functions/crear_cuenta.html",form=form)
    
    if request.method == "POST":
        form = FormularioCrearCuenta()
        if form.validate_on_submit():
            #despues de validar creamos el objeto cuenta para bd
            nombre  = form.nombre.data
            tarjeta = form.tarjeta.data
            user_id = current_user.id
            AccountController().create_account(nombre,tarjeta,user_id)
            return redirect("/index")


@login_required
@email_validation
@user_functions.route("/crearingreso",methods=["GET","POST"])
def crear_ingreso():
    if request.method =="GET":
        form = FormularioCrearIngreso()
        return render_template("user_functions/crear_ingreso.html",form=form)
    
    if request.method == "POST":
        form = FormularioCrearIngreso()
        if form.validate_on_submit():
            #despues de validar creamos el objeto ingreso para bd
            nombre  = form.nombre.data
            fecha   = form.fecha.data
            user_id = current_user.id
            monto   = form.monto.data
            IncomeController().create_income(nombre,fecha,monto,user_id)

            #actualizamos el saldo de la cuenta del usuario
            usuario = User().get_by_id(current_user.id)
            usuario.balance = usuario.balance + monto
            UserController().update_user(usuario)
            return redirect("/index")


@login_required
@email_validation
@user_functions.route("/crearservicio",methods=["GET","POST"])
def crear_servicio():
    if request.method == "GET":
        form = FormularioCrearServicio()
        accounts = Account().get_all_by_userid(current_user.id)#es para la relacion una a muchos entre(cuenta y servicios)
        return render_template("user_functions/crear_servicio.html",form=form,accounts=accounts)
    
    if request.method == "POST":
        form = FormularioCrearServicio()
        if form.validate_on_submit():
            #despues de validar creamos el objeto servicio para bd
            nombre      = form.nombre.data
            descripcion = form.descripcion.data
            fecha       = form.fecha.data
            vencimiento = form.fecha_vencimiento.data
            categoria   = form.categoria.data
            precio      = form.precio.data
            user_id     = current_user.id
            cuenta      = int(request.form.get("cuenta"))
            ServiceController().create_service(nombre,descripcion,fecha,categoria,user_id,precio,precio,cuenta,vencimiento)
            return redirect("/index")

@login_required
@email_validation
@user_functions.route("/crearprestamo",methods=["GET","POST"])
def crear_prestamo():
    if request.method == "GET":
        form     = FormularioCrearPrestamos()
        accounts = Account().get_all_by_userid(current_user.id)#es para la relacion una a muchos entre(cuenta y prestamos)
        return render_template("user_functions/crear_prestamo.html",form=form,accounts=accounts)
    
    if request.method == "POST":
        form = FormularioCrearPrestamos()
        if form.validate_on_submit():
            #despues de validar creamos el objeto prestamo para bd
            nombre   = form.nombre.data
            titular  = form.titular.data 
            precio   = form.precio.data
            cuota    = form.cuota.data
            user_id  = current_user.id
            tea      = form.tea.data
            tea_mora = form.tea_mora.data
            fecha    = form.fecha.data
            vencimiento = form.fecha_vencimiento.data
            cuenta   = int(request.form.get("cuenta"))
            LoanController().create_loan(nombre,titular,precio,cuota,user_id,cuenta,precio,fecha,vencimiento,tea,tea_mora)
            return redirect("/index")
        else:
            return render_template("user_functions/crear_prestamo.html",form=form)

@login_required
@email_validation
@user_functions.route("/pagoprestamo",methods=["GET","POST"])
def pago_prestamo():
    if request.method =="GET":
        form  = FormularioCrearPagoPrestamo()
        loans = Loan().get_all_for_payment(current_user.id)#es para la relacion una a muchos entre(prestamos y prestamos pagados)
        return render_template("user_functions/crear_pago_prestamo.html",form=form,loans=loans)
    
    if request.method =="POST":
        form = FormularioCrearPagoPrestamo()
        if form.validate_on_submit:
            #una vez validamos el formulario, evaluamos que el usuario tenga monto suficiente
            user = User().get_by_id(current_user.id)
            if user.balance < form.monto.data:
                flash("Monto insuficiente","error")
                return redirect("/pagoprestamo")
            else:
                prestamo_id = int(request.form.get("prestamo"))
                monto       = form.monto.data
                prestamo = Loan().get_by_id(prestamo_id)
                
                #Evaluamos si el usuario pago mas de lo que cuesta 
                if monto > prestamo.reamining_price:
                    monto = prestamo.reamining_price
                else:
                    monto  = form.monto.data

                fecha       = form.fecha.data
                descrip     = form.descripcion.data
                #creamos el objeto prestamo_pagado para bd
                LoanPaymentController().create_loan_payment(monto,fecha,descrip,prestamo_id)

                #actualizamos el monto restante para pagar el prestamo
                prestamo.reamining_price = prestamo.reamining_price -monto
                LoanController().update_loan(prestamo)
                #actualizamos el saldo de la cuenta de usuario

                user = User().get_by_id(current_user.id)
                user.balance = user.balance -monto
                UserController().update_user(user)
                return redirect("/index")
        else:
            return "error"

@login_required
@email_validation
@user_functions.route("/pagoservicio",methods=["GET","POST"])
def pago_servicio():
    if request.method == "GET":
        form     = FormularioCrearPagoServicio()
        services = Service().get_all_for_payment(current_user.id)#es para la relacion una a muchos entre(Servicio y pago de servicios)
        return render_template("user_functions/crear_pago_servicio.html",form=form,services=services)
    
    if request.method == "POST":
        form = FormularioCrearPagoServicio()
        if form.validate_on_submit():
            #una vez validamos el formulario, evaluamos que el usuario tenga monto suficiente
            user = User().get_by_id(current_user.id)
            if user.balance < form.monto.data:
                flash("Monto insuficiente","error")
                return redirect("/pagoservicio")
            else:
                servicio_id    = int(request.form.get("servicio"))
                monto          = form.monto.data
                servicio = Service().get_by_id(servicio_id)

                #Evaluamos si el usuario pago mas de lo que cuesta 
                if monto > servicio.reamining_price:
                    monto = servicio.reamining_price
                else:
                    monto  = form.monto.data
                fecha          = form.fecha.data
                descripcion    = form.descripcion.data
                #creamos el objeto servicio_pagado para bd
                ServicePaymentController().create_service_payment(monto,fecha,descripcion,servicio_id)

                #actualizamos el monto restante para pagar el servicio
                servicio.reamining_price = servicio.reamining_price-monto
                ServiceController().update_service(servicio)

                #actualizamos el monto de la cuenta usuario
                user = User().get_by_id(current_user.id)
                user.balance = user.balance -monto
                UserController().update_user(user)
                return redirect("/index")
        else:
            return "error"
        

@user_functions.route("/conf_email/<token>")
@login_required
def confirm_email(token):
    if current_user.email_conf:
        return redirect("/index")
    email = confirm_token(token)
    user = User().get_by_id(current_user.id)
    print(f"{email}=={user.email}")
    if user.email == email:
        user.email_conf= True
        UserController().update_user(user)
        flash("Cuenta confirmada")
        return redirect("/index")
    else:
        flash("Token invalido puto")
        #aqui añadir que muestre token vencido
        print(True if "gerard"==True else False)
        return "xd"

@user_functions.route("/reenviartoken")
@login_required
def reenviar_token():
    user  = User().get_by_id(current_user.id)
    token = genera_token(user.email)
    send_gmail_confirmation(token)
    return redirect("https://mail.google.com/")

@login_required
@email_validation
@user_functions.route("/cerrar_sesion")
def cerrar():
    logout_user()
    return redirect("/")
