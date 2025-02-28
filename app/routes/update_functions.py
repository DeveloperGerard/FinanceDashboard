"""
Funciones del usuario

"""

#modulos externos
from flask                                import Blueprint,render_template,redirect,request
from flask_login                          import current_user,login_required

#modulos propios
from app.forms.importaciones              import FormularioActualizarIngresoProgramado
from app.forms.importaciones              import FormularioActualizarCuenta,FormularioActualizarIngreso,FormularioActualizarPagoPrestamo,FormularioActualizarPrestamos,FormularioActualizarServicio,FormularioRecibirIngresoProgramado
from app.controllers.importaciones        import AccountController,IncomeController,UserController,ServiceController,LoanController,ScheduledIncomeController
from app.models.importaciones             import Income,Account,User,Service,Loan,Scheduled_income,Loan_payment
from ..extra_functions.email_decorator    import email_validation
#blueprint
update_functions = Blueprint('update_functions',__name__)

@update_functions.route("/recibiringresoprogramado",methods=["GET","POST"])
@login_required
@email_validation
def recibir_ingreso_programado():
    if request.method =="GET":
        form = FormularioRecibirIngresoProgramado()
        scheduled_incomes = Scheduled_income().get_all_for_payment(current_user.id)#renderizamos con ingresos programados para que el usuario escoga cual actualizar
        return render_template("update_functions/recibir_schinc.html",form=form,scheduled_incomes=scheduled_incomes)
    
    if request.method == "POST":
        form = FormularioRecibirIngresoProgramado()
        if form.validate_on_submit():
            usuario         = User().get_by_id(current_user.id)

            #despues de validar actualizamos la informacion del objeto ingreso_programado
            scheduled_income                 = Scheduled_income().get_by_id(request.form.get('ingreso_programado'))
            scheduled_income.next_income     = form.proximo_pago.data
            #recibo 50000 y el monto recibiras es 30000
            if form.monto_recibido.data>scheduled_income.amount:
                scheduled_income.received_amount = scheduled_income.amount
                #actualizamos el saldo de la cuenta del usuario con el monto pendiente si el monto recibido es mayor al que esperamos
                usuario.balance = usuario.balance + scheduled_income.pending_amount
                print("Entro a aqui 1")
            else:
                print("Entro a aqui 2")
                scheduled_income.received_amount = form.monto_recibido.data + scheduled_income.received_amount
                #actualizamos el saldo de la cuenta del usuario con el monto recibido del form si es que no supera el monto limite establecido
                usuario.balance = usuario.balance + form.monto_recibido.data
            
            #estable el monto pendiente en 0 si el monto que recibimos es mayor al pendiente
            if form.monto_recibido.data >= scheduled_income.pending_amount:
                scheduled_income.pending_amount = 0
            else:
            #establecemos el monto pendiente como la resta del monto final con el monto recibido
                scheduled_income.pending_amount  = scheduled_income.amount - form.monto_recibido.data

            ScheduledIncomeController().update_income(scheduled_income)
            UserController().update_user(usuario)
            return redirect("/index")

@update_functions.route("/actualizaringresoprogramado",methods=["GET","POST"])
@login_required
@email_validation
def actualizar_ingreso_programado():
    if request.method =="GET":
        form = FormularioActualizarIngresoProgramado()
        scheduled_incomes = Scheduled_income().get_all_for_payment(current_user.id)#renderizamos con ingresos programados para que el usuario escoga cual actualizar
        return render_template("update_functions/actualizar_shinc.html",form=form,scheduled_incomes=scheduled_incomes)
    
    if request.method == "POST":
        form = FormularioActualizarIngresoProgramado()
        if form.validate_on_submit():
            nombre       = form.nombre.data
            descripcion  = form.descripcion.data
            categoria    = form.categoria.data
            monto        = form.monto.data
            proximo_pago = form.proximo_pago.data
            scheduled_income = Scheduled_income().get_by_id(int(request.form.get("ingreso_programado")))
            scheduled_income.income_name = nombre
            scheduled_income.next_income = proximo_pago
            scheduled_income.category = categoria
            scheduled_income.description = descripcion
            scheduled_income.amount = monto
            ScheduledIncomeController().update_income(scheduled_income) 
            return redirect("/index")

@update_functions.route("/actualizar_cuenta",methods=["GET","POST"])
@login_required
@email_validation
def actualizar_cuenta():
    if request.method == "GET":
        form     = FormularioActualizarCuenta()
        accounts = Account().get_all_by_userid(current_user.id)
        return render_template("update_functions/actualizar_cuenta.html",form=form,accounts=accounts)
    if request.method == "POST":
        form = FormularioActualizarCuenta()
        if form.validate_on_submit():
            nombre  = form.nombre.data
            tarjeta = form.tarjeta.data
            account = Account().get_by_id(int(request.form.get("account")))
            account.account_name = nombre  if nombre  !="" else account.account_name
            account.card         = tarjeta if tarjeta !="" else account.card
            AccountController().update_account(account)
            return redirect("/")


        
@update_functions.route("/actualizar_ingreso",methods=["GET","POST"])
@login_required
@email_validation
def actualizar_ingreso():
    if request.method =="GET":
        form    = FormularioActualizarIngreso()
        incomes = Income().get_all_by_userid(current_user.id)
        return render_template("update_functions/actualizar_ingreso.html",form=form,incomes=incomes)
    if request.method == "POST":
        form    = FormularioActualizarIngreso()
        if form.validate_on_submit():
            nombre          = form.nombre.data
            fecha           = form.fecha_pago.data
            descripcion     = form.descripcion.data
            categoria       = form.categoria.data
            monto           = form.monto.data
            income = Income().get_by_id(int(request.form.get("income")))
            income.income_name = nombre
            income.income_date = fecha
            income.description = descripcion
            income.amount      = monto
            income.category    = categoria
            IncomeController().update_income(income)
            return redirect("/")
        
@update_functions.route("/actualizar_prestamo",methods=["GET","POST"])
@login_required
@email_validation
def actualizar_prestamo():
    if request.method == "GET":
        form  = FormularioActualizarPrestamos()
        loans = Loan().get_all_by_userid(current_user.id) 
        return render_template("update_functions/actualizar_prestamo.html",form=form,loans=loans)
    if request.method == "POST":
        form  = FormularioActualizarPrestamos()
        if form.validate_on_submit():
            nombre      = form.nombre.data
            titular     = form.titular.data 
            precio      = form.precio.data
            cuota       = form.cuota.data
            tea         = form.tea.data
            vencimiento = form.fecha_vencimiento.data
            loan = Loan().get_by_id(int(request.form.get("loan")))
            loan.loan_name       = nombre
            loan.holder          = titular
            loan.price           = precio
            loan.quota           = cuota
            loan.tea             = tea
            loan.expiration_date = vencimiento
            loan.reamining_price = precio
            LoanController().update_loan(loan)
            return redirect("/")

@update_functions.route("/actualizar_servicio",methods=["GET","POST"])
@login_required
@email_validation
def actualizar_servicio():
    if request.method == "GET":
        form = FormularioActualizarServicio()
        services = Service().get_all_by_userid(current_user.id)
        return render_template("update_functions/actualizar_servicio.html",form=form,services=services)
    if request.method == "POST":
        form = FormularioActualizarServicio()
        if form.validate_on_submit():
            nombre      = form.nombre.data
            descripcion = form.descripcion.data
            vencimiento = form.fecha_vencimiento.data
            categoria   = form.categoria.data
            precio      = form.precio.data
            service     = Service().get_by_id(int(request.form.get("service")))
            service.service_name    = nombre
            service.description     = descripcion 
            service.expiration_date = vencimiento
            service.category        = categoria
            service.price           = precio
            service.reamining_price = precio
            ServiceController().update_service(service)
            return redirect("/")