from flask import Blueprint, render_template,redirect,request
from flask_login import login_required ,LoginManager,current_user,login_user,logout_user
from ..forms.form_user import FormularioInicio,FormularioRegistro
from ..models.user import User
from werkzeug.security import generate_password_hash, check_password_hash 
from ..controllers.user_controller import UserController
main= Blueprint('main', __name__) 

@main.route('/') 
@main.route('/index') 
def index(): 
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        return redirect("/iniciar")


    
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
        
@main.route('/iniciar',methods=["GET","POST"])
def inicio_sesion():
    if request.method =="GET":
        login = FormularioInicio()
        return render_template("login.html",login=login)
    elif request.method=="POST":
        login_e = FormularioInicio()
        email = login_e.email.data
        if login_e.validate_on_submit():
            user  = User().get_by_email(email)
            if user is None:
                return "usuario no existe"
            else:
                print("--------------------------------------------------")
                print(user.username)
                print(user.password_hash)
                print(user.email)
                print(login_e.clave.data)
                print(user.check_password("12345678"))
                print(check_password_hash(user.password_hash,"12345678"))
                print("--------------------------------------------------")
                if user.check_password(login_e.clave.data):
                    login_user(user)
                    print("contraseña buena")
                    return redirect("/home") 
                else:
                    print(user.password_hash)
                    print(login_e.clave.data)
                    print("contraseña mala")    
                    return render_template("login.html",login=login_e)   
                
@login_required
@main.route("/home")
def saludo():
    user = User().get_by_id(current_user.id)
    print(current_user.username)
    return render_template("prueba.html",user=user)
@login_required
@main.route("/cerrar_sesion")
def cerrar():
    logout_user()
    return redirect("/")
