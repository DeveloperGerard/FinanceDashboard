from flask import Blueprint, render_template, redirect, url_for
from flask_login import login_required, current_user, logout_user

# Crear el Blueprint
main = Blueprint('main', __name__)

# Ruta principal
@main.route('/')
@main.route('/index')
def index():
    # Redirigir al dashboard si el usuario está autenticado
    if current_user.is_authenticated:
        return redirect(url_for('main.dashboard'))
    return redirect(url_for('main.login'))  # Redirigir al login si no está autenticado

# Ruta para la página de inicio de sesión
@main.route('/login')
def login():
    return render_template('login.html')

@main.route('/register')
def register():
    return render_template('register.html')

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
