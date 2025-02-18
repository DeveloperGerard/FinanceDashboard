from flask                          import Blueprint,render_template,redirect,request,flash,jsonify,url_for
from flask_login                    import current_user,login_required
from app.forms.form_income          import FormularioCrearIngreso
from app.forms.form_account         import FormularioActualizarCuenta,FormularioCrearCuenta
from app.forms.form_service         import FormularioCrearServicio
from app.forms.form_loanpayments    import FormularioCrearPagoPrestamo
from app.forms.form_servicepayments import FormularioCrearPagoServicio
from app.forms.form_loan            import FormularioCrearPrestamos
from app.controllers.importaciones  import AccountController,IncomeController,UserController,ServiceController,LoanController,LoanPaymentController,ServicePaymentController
from app.models.importaciones       import Income,Account,User,Service,Loan
from .. import db

user_functions = Blueprint('user_functions',__name__)

"""
Aqui van a estar las rutas relacionadas con las funciones que 
puede realizar el usuario como crear prestamos,servicios,etc.

"""

@user_functions.route("/crear_cuenta", methods=["POST"])
@login_required
def crear_cuenta():
    try:
        account_name = request.form['account_name']
        card = request.form['card']
        balance = float(request.form['balance'])

        print(f"Received data: account_name={account_name}, card={card}, balance={balance}")

        new_account = Account(
            account_name=account_name,
            card=card,
            balance=balance,
            user_id=current_user.id
        )
        db.session.add(new_account)
        db.session.commit()
        flash('Cuenta agregada exitosamente', 'success')
        return redirect(url_for('user.accounts'))
    except Exception as e:
        print(f"Error: {str(e)}")
        flash(f'Error al crear cuenta: {str(e)}', 'error')
        return redirect(url_for('user.accounts'))



@user_functions.route("/crearingreso", methods=["POST"])
@login_required
def crear_ingreso():
    try:
        income_name = request.form['income_name']
        amount = float(request.form['amount'])
        date = request.form['date']

        print(f"Received data: income_name={income_name}, amount={amount}, date={date}")

        new_income = Income(
            income_name=income_name,
            amount=amount,
            date=date,
            user_id=current_user.id
        )
        db.session.add(new_income)
        db.session.commit()
        flash('Ingreso agregado exitosamente', 'success')
        return redirect(url_for('user.incomes'))
    except Exception as e:
        print(f"Error: {str(e)}")
        flash(f'Error al crear ingreso: {str(e)}', 'error')
        return redirect(url_for('user.incomes'))


@user_functions.route("/crearservicio", methods=["POST"])
@login_required
def crear_servicio():
    try:
        service_name = request.form['service_name']
        description = request.form['description']
        date = request.form['date']
        category = request.form['category']
        price = float(request.form['price'])
        reamining_price = price  # Automatically set the outstanding balance to the price

        print(f"Received data: service_name={service_name}, description={description}, date={date}, category={category}, price={price}")

        new_service = Service(
            service_name=service_name,
            description=description,
            date=date,
            category=category,
            price=price,
            reamining_price=reamining_price,
            user_id=current_user.id
        )
        db.session.add(new_service)
        db.session.commit()
        flash('Servicio agregado exitosamente', 'success')
        return redirect(url_for('user.services'))
    except Exception as e:
        print(f"Error: {str(e)}")
        flash(f'Error al crear servicio: {str(e)}', 'error')
        return redirect(url_for('user.services'))



@user_functions.route("/crear_prestamo", methods=["POST"])
@login_required
def crear_prestamo():
    try:
        loan_name = request.form['loan_name']
        holder = request.form['holder']
        price = float(request.form['price'])
        quota = request.form.get('quota', None)
        tea = float(request.form['tea'])
        reamining_price = float(request.form['reamining_price'])

        new_loan = Loan(
            loan_name=loan_name,
            holder=holder,
            price=price,
            quota=quota,
            tea=tea,
            reamining_price=reamining_price,
            user_id=current_user.id
        )
        db.session.add(new_loan)
        db.session.commit()
        flash('Préstamo creado exitosamente', 'success')
        return redirect(url_for('user.loans'))
    except Exception as e:
        flash(f'Error al crear préstamo: {str(e)}', 'danger')
        return redirect(url_for('user.loans'))

@login_required
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
        
@user_functions.route("/eliminar_prestamo/<int:loan_id>", methods=["POST"])
@login_required
def eliminar_prestamo(loan_id):
    try:
        loan = Loan.query.get(loan_id)
        if not loan:
            flash('Préstamo no encontrado', 'danger')
            return redirect(url_for('user.loans'))
            
        if loan.user_id != current_user.id:
            flash('No tienes permiso para eliminar este préstamo', 'danger')
            return redirect(url_for('user.loans'))
        
        db.session.delete(loan)
        db.session.commit()
        flash('Préstamo eliminado exitosamente', 'success')
        return redirect(url_for('user.loans'))
    except Exception as e:
        flash(f'Error al eliminar préstamo: {str(e)}', 'danger')
        return redirect(url_for('user.loans'))

@user_functions.route("/cambiar_estado_prestamo/<int:loan_id>", methods=["POST"])
@login_required
def cambiar_estado_prestamo(loan_id):
    try:
        loan = Loan.query.get(loan_id)
        if not loan:
            flash('Préstamo no encontrado', 'danger')
            return redirect(url_for('user.loans'))
            
        if loan.user_id != current_user.id:
            flash('No tienes permiso para cambiar el estado de este préstamo', 'danger')
            return redirect(url_for('user.loans'))
        
        loan.reamining_price = 0 if loan.reamining_price > 0 else loan.price
        db.session.commit()
        flash('Estado del préstamo cambiado exitosamente', 'success')
        return redirect(url_for('user.loans'))
    except Exception as e:
        flash(f'Error al cambiar el estado del préstamo: {str(e)}', 'danger')
        return redirect(url_for('user.loans'))
    
@user_functions.route("/eliminar_servicio/<int:service_id>", methods=["POST"])
@login_required
def eliminar_servicio(service_id):
    try:
        service = Service.query.get(service_id)
        if not service:
            flash('Servicio no encontrado', 'danger')
            return redirect(url_for('user.services'))

        if service.user_id != current_user.id:
            flash('No tienes permiso para eliminar este servicio', 'danger')
            return redirect(url_for('user.services'))

        db.session.delete(service)
        db.session.commit()
        flash('Servicio eliminado exitosamente', 'success')
        return redirect(url_for('user.services'))
    except Exception as e:
        print(f"Error: {str(e)}")
        flash(f'Error al eliminar servicio: {str(e)}', 'error')
        return redirect(url_for('user.services'))

    
@user_functions.route("/eliminar_ingreso/<int:income_id>", methods=["POST"])
@login_required
def eliminar_ingreso(income_id):
    try:
        income = Income.query.get(income_id)
        if not income:
            flash('Ingreso no encontrado', 'danger')
            return redirect(url_for('user.incomes'))
            
        if income.user_id != current_user.id:
            flash('No tienes permiso para eliminar este ingreso', 'danger')
            return redirect(url_for('user.incomes'))
        
        db.session.delete(income)
        db.session.commit()
        flash('Ingreso eliminado exitosamente', 'success')
        return redirect(url_for('user.incomes'))
    except Exception as e:
        print(f"Error: {str(e)}")
        flash(f'Error al eliminar ingreso: {str(e)}', 'error')
        return redirect(url_for('user.incomes'))

@user_functions.route("/eliminar_cuenta/<int:account_id>", methods=["POST"])
@login_required
def eliminar_cuenta(account_id):
    try:
        account = Account.query.get(account_id)
        if not account:
            flash('Cuenta no encontrada', 'danger')
            return redirect(url_for('user.accounts'))
            
        if account.user_id != current_user.id:
            flash('No tienes permiso para eliminar esta cuenta', 'danger')
            return redirect(url_for('user.accounts'))

        db.session.delete(account)
        db.session.commit()
        flash('Cuenta eliminada exitosamente', 'success')
        return redirect(url_for('user.accounts'))
    except Exception as e:
        print(f"Error: {str(e)}")
        flash(f'Error al eliminar cuenta: {str(e)}', 'error')
        return redirect(url_for('user.accounts'))



