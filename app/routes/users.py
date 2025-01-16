from flask import Blueprint, render_template,redirect,request
from flask_login import login_required ,LoginManager,current_user,login_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from ..models.user import User
from ..controllers.user_controller import UserController
main= Blueprint('main', __name__) 

@main.route('/') 
@main.route('/index') 
def index(): 
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        return redirect("/iniciar")

@main.route('/iniciar',methods=["GET","POST"])
def inicio_sesion():
    login = FormularioInicio()
    if request.method =="GET":
        return render_template("login.html",login=login)
    
@main.route('/registro',methods=["GET","POST"])
def registro():
    registro =   FormularioRegistro()

    if request.method =="GET":
        return render_template("register.html",registro=registro)  
    
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
                return redirect("/iniciar")
            elif usuario_nombre:
                return redirect("/iniciar")
            else:
                #Si no ahy duplicados se crea usuario y se abre sesion
                nombre = registro.nombre.data
                email  = registro.email.data
                clave  = registro.clave.data
                UserController().create_user(nombre,email,clave)
                user = User().get_by_email(email)
                login_user(user)
                return redirect("/index")
        else:
            return redirect("/registro")
@login_required
@main.route("/home")
def saludo():
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("prueba.html",user=user)
    