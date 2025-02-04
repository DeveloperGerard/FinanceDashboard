"""
Rutas publicas

"""

from flask import Blueprint, render_template,redirect,request,flash
from flask_login import login_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from ..controllers.user_controller import UserController
from ..models.user import User
from ..funciones.notification_funct import send_gmail,send_gmail_confirmation
from ..funciones.token import genera_token
public= Blueprint('public', __name__) 

@public.route('/registro',methods=["GET","POST"])
def registro():
    registro =   FormularioRegistro()

    if request.method =="GET":
        return render_template("public/register.html",registro=registro)  
    
    elif request.method =="POST":
        registro = FormularioRegistro()
        if registro.validate_on_submit():
            email          = registro.email.data
            name           = registro.nombre.data
            usuario_email  = User().get_by_email(email)
            usuario_nombre = User().get_by_name(name)

            #Evitar que se dupliquen email y nombre.
            #faltan añadir mensajes de respuesta
            if usuario_email:
                flash(f"Ese email ya esta registrado","error")
                return redirect("/registro")
            elif usuario_nombre:
                flash(f"Ese nombre ya esta registrado usa otro","error")
                return redirect("/registro")
            else:
                #Si no ahy duplicados se crea usuario y se abre sesion
                nombre = registro.nombre.data
                email  = registro.email.data
                clave  = registro.clave.data
                UserController().create_user(nombre,email,clave)
                user = User().get_by_email(email)
                login_user(user)
                send_gmail(email)
                token = genera_token(user.email)
                send_gmail_confirmation(token)
                return redirect("/index")
        else:
            return redirect("/registro")
        
@public.route('/iniciar',methods=["GET","POST"])
def inicio_sesion():
    if request.method =="GET":
        login = FormularioInicio()
        return render_template("public/login.html",login=login)
    elif request.method=="POST":
        login_e = FormularioInicio()
        email = login_e.email.data
        if login_e.validate_on_submit():
            user  = User().get_by_email(email)
            if user is None:
                flash(f"Ese usuario no esta registrado","error")
                return redirect("/iniciar")
            else:
                if user.check_password(login_e.clave.data):
                    login_user(user)
                    return redirect("/home") 
                else:  
                    flash(f"Contraseña incorrecta","error")
                    return redirect("/iniciar")

