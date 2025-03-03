"""
Funciones de creacion
"""



#modulos externos
from flask                                import Blueprint,render_template,redirect,request,flash
from flask_login                          import current_user,login_required
from datetime import datetime
#modulos propios
from app.forms.importaciones              import FormularioCrearPrestamos,FormularioCrearPagoServicio,FormularioCrearPagoPrestamo,FormularioCrearServicio,FormularioCrearCuenta,FormularioCrearIngresoProgamado,FormularioCrearIngreso
from app.controllers.importaciones        import AccountController,IncomeController,UserController,ServiceController,LoanController,LoanPaymentController,ServicePaymentController,ScheduledIncomeController
from app.models.importaciones             import Account,User,Service,Loan
from ..extra_functions.email_decorator    import email_validation
from ..extra_functions.calcular_tem       import calcular_tem

create_functions= Blueprint('create_functions', __name__)


@create_functions.route("/crearcuenta",methods=["GET","POST"])
@login_required
@email_validation
def crear_cuenta():
    if request.method =="GET":
        form = FormularioCrearCuenta()
        return render_template("create_functions/crear_cuenta.html",form=form)
    
    if request.method == "POST":
        form = FormularioCrearCuenta()
        if form.validate_on_submit():

            #despues de validar creamos el objeto cuenta para bd
            nombre  = form.nombre.data
            tarjeta = form.tarjeta.data
            AccountController().create_account(nombre,tarjeta,current_user.id)
            return redirect("/index")

@create_functions.route("/crearingreso",methods=["GET","POST"])
@login_required
@email_validation
def crear_ingreso():
    if request.method =="GET":
        form = FormularioCrearIngreso()
        return render_template("create_functions/crear_ingreso.html",form=form)
    
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


@create_functions.route("/crearingresoprogramado",methods=["GET","POST"])
@login_required
@email_validation
def crear_ingreso_programado():
    if request.method =="GET":
        form = FormularioCrearIngresoProgamado()
        return render_template("create_functions/crear_ingreso_programado.html",form=form)
    
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

@create_functions.route("/crearservicio",methods=["GET","POST"])
@login_required
@email_validation
def crear_servicio():
    if request.method == "GET":
        form = FormularioCrearServicio()
        accounts = Account().get_all_by_userid(current_user.id)#es para la relacion una a muchos entre(cuenta y servicios)
        return render_template("create_functions/crear_servicio.html",form=form,accounts=accounts)
    
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


@create_functions.route("/crearprestamo",methods=["GET","POST"])
@login_required
@email_validation
def crear_prestamo():
    if request.method == "GET":
        form     = FormularioCrearPrestamos()
        accounts = Account().get_all_by_userid(current_user.id)#es para la relacion una a muchos entre(cuenta y prestamos)
        return render_template("create_functions/crear_prestamo.html",form=form,accounts=accounts)
    
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
            return render_template("create_functions/crear_prestamo.html",form=form)
        
@create_functions.route("/pagoprestamo",methods=["GET","POST"])
@login_required
@email_validation
def pago_prestamo():
    if request.method =="GET":
        form  = FormularioCrearPagoPrestamo()
        loans = Loan().get_all_for_payment(current_user.id)#es para la relacion una a muchos entre(prestamos y prestamos pagados)
        return render_template("create_functions/crear_pago_prestamo.html",form=form,loans=loans)
    
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

                fecha_pago =form.fecha.data  
                tea = prestamo.tea
                if tea >0:
                    if fecha_pago > prestamo.expiration_date:
                        monto =monto+calcular_tem(prestamo.tea,prestamo.quota)*monto 
                        
                descrip = form.descripcion.data
                user_id = current_user.id
                #creamos el objeto prestamo_pagado para bd
                LoanPaymentController().create_loan_payment(monto,fecha_pago,descrip,prestamo_id,user_id)

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

@create_functions.route("/pagoservicio",methods=["GET","POST"])
@login_required
@email_validation
def pago_servicio():
    if request.method == "GET":
        form     = FormularioCrearPagoServicio()
        services = Service().get_all_for_payment(current_user.id)#es para la relacion una a muchos entre(Servicio y pago de servicios)
        return render_template("create_functions/crear_pago_servicio.html",form=form,services=services)
    
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