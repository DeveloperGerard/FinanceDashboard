from flask import Blueprint, render_template,redirect,request,flash
from flask_login import login_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from ..controllers.user_controller import UserController
from ..models.user import User
from ..extra_functions.notification_funct import send_gmail,send_gmail_confirmation
from ..extra_functions.token import genera_token
from ..extra_functions.public_decorator import no_enter

public= Blueprint('public', __name__) 

"""
Aqui van a estar las rutas a las que cualquiera persona 
puede acceder aunque no este registrada

"""
@public.route('/registro', methods=["GET", "POST"])
@no_enter
def registro():
    registro = FormularioRegistro()

    if request.method == "POST":
        if registro.validate_on_submit():
            email = registro.email.data
            name = registro.username.data

            # Verificar si el email o el nombre ya existen
            if User().get_by_email(email):
                flash("Ese email ya está registrado", "error")
            elif User().get_by_name(name):
                flash("Ese nombre ya está registrado, usa otro", "error")
            else:
                # Si no hay duplicados, crear usuario y enviar correo
                UserController().create_user(name, email, registro.clave.data)
                user = User().get_by_email(email)
                login_user(user)
                send_gmail(email)
                token = genera_token(user.email)
                send_gmail_confirmation(token)
                return redirect("/index")
            return redirect("/registro")

    return render_template("register.html", registro=registro)

        
@public.route('/iniciar', methods=["GET", "POST"])
@no_enter
def inicio_sesion():
    login = FormularioInicio()  # Instanciar el formulario correctamente

    if login.validate_on_submit():  # Verifica que el formulario es válido y el CSRF token está correcto
        email = login.email.data
        user = User().get_by_email(email)

        if user is None:
            flash("Ese usuario no está registrado", "error")
        elif user.check_password(login.clave.data):
            login_user(user)
            return redirect("/home")
        else:
            flash("Contraseña incorrecta", "error")

    # Si hay errores o es un GET, vuelve a mostrar el formulario con los errores
    return render_template("login.html", login=login)
