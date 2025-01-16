from flask import Blueprint, render_template, redirect, request, url_for
from flask_login import login_required, current_user, logout_user
from ..forms.form_user import FormularioInicio,FormularioRegistro

# Crear el Blueprint
main = Blueprint('main', __name__)

# Ruta principal
@main.route('/')
@main.route('/index')
def index():
    return render_template('bienvenida.html')

# Ruta para la página de inicio de sesión
@main.route('/iniciar',methods=["GET","POST"])
def inicio_sesion():
    login = FormularioInicio()
    if request.method =="GET":
        return render_template("login.html",login=login)
    
# Ruta para la página de registro
@main.route('/register',methods=["GET","POST"])
def registro():
    register =   FormularioRegistro()
    if request.method =="GET":
        return render_template("register.html",register=register)  

# Ruta para el dashboard, solo accesible para usuarios autenticados
@main.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', user=current_user)

# Ruta para cerrar sesión
@main.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('main.login'))
