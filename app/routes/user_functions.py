"""
Funciones del usuario

"""

#modulos externos
from flask                                import Blueprint,render_template,redirect,request,flash
from flask_login                          import current_user,login_required,logout_user
from datetime import datetime
#modulos propios
from app.forms.importaciones              import FormularioCrearPrestamos,FormularioCrearPagoServicio,FormularioCrearPagoPrestamo,FormularioCrearServicio,FormularioCrearCuenta,FormularioCrearIngresoProgamado,FormularioCrearIngreso,FormularioActualizarIngresoProgramado
from app.controllers.importaciones        import AccountController,IncomeController,UserController,ServiceController,LoanController,LoanPaymentController,ServicePaymentController,ScheduledIncomeController
from app.models.importaciones             import Income,Account,User,Service,Loan,Scheduled_income
from ..extra_functions.token              import confirm_token,genera_token
from ..extra_functions.notification_funct import send_gmail_confirmation
from ..extra_functions.email_decorator    import email_validation

#blueprint
user_functions = Blueprint('user_functions',__name__)

@user_functions.route("/crearcuenta",methods=["GET","POST"])
@login_required
@email_validation
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
            AccountController().create_account(nombre,tarjeta,current_user.id)
            return redirect("/index")

@user_functions.route("/crearingreso",methods=["GET","POST"])
@login_required
@email_validation
def crear_ingreso():
    if request.method =="GET":
        form = FormularioCrearIngreso()
        return render_template("user_functions/crear_ingreso.html",form=form)
    
    if request.method == "POST":
        form = FormularioCrearIngreso()
        if form.validate_on_submit():

            #despues de validar creamos el objeto ingreso para bd
            nombre          = form.nombre.data
            fecha           = form.fecha_pago.data
            descripcion     = form.descripcion.data
            categoria       = form.categoria.data
            monto           = form.monto.data
            IncomeController().create_income(nombre,fecha,monto,current_user.id,descripcion,categoria)

            #actualizamos el saldo de la cuenta del usuario
            usuario         = User().get_by_id(current_user.id)
            usuario.balance = usuario.balance + monto
            UserController().update_user(usuario)
            return redirect("/index")

@user_functions.route("/actualizaringresoprogramado",methods=["GET","POST"])
@login_required
@email_validation
def actualizar_ingreso_programado():
    if request.method =="GET":
        form = FormularioActualizarIngresoProgramado()
        scheduled_incomes = Scheduled_income().get_all_for_payment(current_user.id)#renderizamos con ingresos programados para que el usuario escoga cual actualizar
        return render_template("user_functions/actualizar_schinc.html",form=form,scheduled_incomes=scheduled_incomes)
    
    if request.method == "POST":
        form = FormularioActualizarIngresoProgramado()
        if form.validate_on_submit():
            usuario         = User().get_by_id(current_user.id)

            #despues de validar actualizamos la informacion del objeto ingreso_programado
            scheduled_income                 = Scheduled_income().get_by_id(request.form.get('ingreso_programado'))
            scheduled_income.next_income     = form.proximo_pago.data
            #recibo 50000 y el monto recibiras es 30000
            if form.monto_recibido.data>scheduled_income.amount:
                scheduled_income.received_amount = scheduled_income.amount
                #actualizamos el saldo de la cuenta del usuario
                usuario.balance = usuario.balance + scheduled_income.pending_amount
                print("Entro a aqui 1")
            else:
                print("Entro a aqui 2")
                scheduled_income.received_amount = form.monto_recibido.data + scheduled_income.received_amount
                #actualizamos el saldo de la cuenta del usuario con el monto recibido del form si es que no supera el monto limite establecido
                usuario.balance = usuario.balance + form.monto_recibido.data

            if form.monto_recibido.data >= scheduled_income.pending_amount:
                scheduled_income.pending_amount = 0
            else:
                scheduled_income.pending_amount  = scheduled_income.amount - form.monto_recibido.data

            ScheduledIncomeController().update_income(scheduled_income)
            #si el monto recivido es mayor que el pendiente simplemente lo deja en 0 y le suma lo que faltava al usuario

            UserController().update_user(usuario)
            return redirect("/index")

@user_functions.route("/crearingresoprogramado",methods=["GET","POST"])
@login_required
@email_validation
def crear_ingreso_programado():
    if request.method =="GET":
        form = FormularioCrearIngresoProgamado()
        return render_template("user_functions/crear_ingreso_programado.html",form=form)
    
    if request.method == "POST":
        form = FormularioCrearIngresoProgamado()
        if form.validate_on_submit():

            #despues de validar creamos el objeto ingreso programado para bd
            nombre          = form.nombre.data
            fecha           = datetime.now()
            descripcion     = form.descripcion.data
            categoria       = form.categoria.data
            proximo_pago    = form.proximo_pago.data
            monto           = form.monto.data
            ScheduledIncomeController().create_income(nombre,fecha,monto,current_user.id,descripcion,categoria=categoria,next_income=proximo_pago,received_amount=0,pending_amount=monto)
            return redirect("/index")

@user_functions.route("/crearservicio",methods=["GET","POST"])
@login_required
@email_validation
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
            fecha       = datetime.now()
            vencimiento = form.fecha_vencimiento.data
            categoria   = form.categoria.data
            precio      = form.precio.data
            cuenta      = int(request.form.get("cuenta"))
            ServiceController().create_service(nombre,descripcion,fecha,categoria,current_user.id,precio,precio,cuenta,vencimiento)
            return redirect("/index")


@user_functions.route("/crearprestamo",methods=["GET","POST"])
@login_required
@email_validation
def crear_prestamo():
    if request.method == "GET":
        form     = FormularioCrearPrestamos()
        accounts = Account().get_all_by_userid(current_user.id)#es para la relacion una a muchos entre(cuenta y prestamos)
        return render_template("user_functions/crear_prestamo.html",form=form,accounts=accounts)
    
    if request.method == "POST":
        form = FormularioCrearPrestamos()
        if form.validate_on_submit():

            #despues de validar creamos el objeto prestamo para bd
            nombre      = form.nombre.data
            titular     = form.titular.data 
            precio      = form.precio.data
            cuota       = form.cuota.data
            tea         = form.tea.data
            fecha       = datetime.now()
            vencimiento = form.fecha_vencimiento.data
            cuenta      = int(request.form.get("cuenta"))
            LoanController().create_loan(nombre,titular,precio,cuota,current_user.id,cuenta,precio,fecha,vencimiento,tea)
            return redirect("/index")
        else:
            return render_template("user_functions/crear_prestamo.html",form=form)


@user_functions.route("/pagoprestamo",methods=["GET","POST"])
@login_required
@email_validation
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

                fecha   = form.fecha.data
                descrip = form.descripcion.data
                user_id = current_user.id
                #creamos el objeto prestamo_pagado para bd
                LoanPaymentController().create_loan_payment(monto,fecha,descrip,prestamo_id,user_id)

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

@user_functions.route("/pagoservicio",methods=["GET","POST"])
@login_required
@email_validation
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
                fecha       = form.fecha.data
                descripcion = form.descripcion.data
                user_id     = current_user.id
                #creamos el objeto servicio_pagado para bd
                ServicePaymentController().create_service_payment(monto,fecha,descripcion,servicio_id,user_id)

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
    if user.email == email:
        user.email_conf= True
        UserController().update_user(user)
        flash("Cuenta confirmada")
        return redirect("/index")
    else:
        flash("Token invalido")
        #aqui añadir que muestre token vencido
        return "xd"

@user_functions.route("/reenviartoken")
@login_required
def reenviar_token():
    user  = User().get_by_id(current_user.id)
    token = genera_token(user.email)
    send_gmail_confirmation(token)
    return redirect("https://mail.google.com/")


@user_functions.route("/cerrar_sesion")
@login_required
@email_validation
def cerrar():
    logout_user()
    return redirect("/")
