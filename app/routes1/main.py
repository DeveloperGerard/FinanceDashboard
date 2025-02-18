from flask import Blueprint, render_template, redirect, request, url_for, flash
from flask_login import login_user, login_required, current_user, logout_user
from ..forms.form_user import FormularioInicio, FormularioRegistro
from ..models.loan import Loan
from ..models.income import Income
from ..models.service import Service
from ..models.account import Account
from ..models.user import User
from .. import db

# Crear el Blueprint
main = Blueprint('main', __name__)

# Ruta principal
@main.route('/')
@main.route('/index')
def index():
    return render_template('bienvenida.html')

@main.route('/register', methods=["GET", "POST"])
def registro():
    register = FormularioRegistro()
    if request.method == "POST" and register.validate_on_submit():
        try:
            # Validate password
            raw_password = register.clave.data
            if not raw_password or len(raw_password) < 8:
                raise ValueError("Password must be at least 8 characters")
                
            # Create user
            new_user = User(
                username=register.username.data,
                email=register.email.data
            )
            new_user.set_password(raw_password)
            
            # Verify password works
            if not new_user.check_password(raw_password):
                raise ValueError("Password verification failed")
                
            db.session.add(new_user)
            db.session.commit()
            
            flash('Registration successful', 'success')
            return redirect(url_for('main.inicio_sesion'))
            
        except Exception as e:
            print(f"Registration error: {str(e)}")
            flash(str(e), 'danger')
            
    return render_template("register.html", register=register)

# Ruta para la página de inicio de sesión
@main.route('/iniciar', methods=["GET", "POST"]) 
def inicio_sesion():
    login = FormularioInicio()
    if request.method == "POST" and login.validate_on_submit():
        try:
            user = User.query.filter_by(email=login.email.data).first()
            print(f"Login attempt for email: {login.email.data}")
            print(f"User found: {user is not None}")
            print(f"Password provided: {login.clave.data}")
            print(f"password hash: {user.password_hash}")
            
            if user:
                valid = user.check_password(login.clave.data)
                print(f"Password valid: {valid}")
                
                if valid:
                    login_user(user)
                    print("User logged in successfully")
                    return redirect(url_for('main.dashboard'))
            
            flash('Invalid username or password', 'danger')
        except Exception as e:
            print(f"Login error: {str(e)}")
            flash(f'An error occurred: {str(e)}', 'danger')
    return render_template("login.html", login=login)



# Ruta para el dashboard, solo accesible para usuarios autenticados
@main.route('/dashboard')
@login_required
def dashboard():
    print(f"Accessing dashboard. User authenticated: {current_user.is_authenticated}")  # Debug dashboard access
    return render_template('index.html', user=current_user)

# Ruta para cerrar sesión
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.inicio_sesion'))

@main.route('/loans')
@login_required
def loans():
    loanss = Loan.query.filter_by(user_id=current_user.id).all()
    return render_template('loan.html', loans=loanss)

@main.route('/add-loan', methods=['POST'])
@login_required
def add_loan():
    loan_name = request.form['loan_name']
    holder = request.form['holder']
    price = int(request.form['price'])
    quota = request.form.get('quota', None)
    tea = request.form.get('tea', None)
    reamining_price = int(request.form['reamining_price'])

    new_loan = Loan(
        loan_name=loan_name,
        holder=holder,
        price=price,
        quota=quota,
        tea=tea,
        reamining_price=reamining_price,
        user_id=current_user.id  # Use the ID of the authenticated user
    )
    db.session.add(new_loan)
    db.session.commit()
    flash('Préstamo agregado exitosamente', 'success')
    return redirect(url_for('user.loans'))

@main.route('/services')
@login_required
def services():
    services = Service.query.filter_by(user_id=current_user.id).all()
    return render_template('services.html', services=services)

@main.route('/incomes')
@login_required
def incomes():
    incomes = Income.query.filter_by(user_id=current_user.id).all()
    return render_template('incomes.html', incomes=incomes)

@main.route('/accounts')
@login_required
def accounts():
    accounts = Account.get_all_by_userid(current_user.id)
    return render_template('accounts.html', accounts=accounts)

@login_required
@main.route("/cerrar_sesion")
def cerrar():
    logout_user()
    return redirect("/")