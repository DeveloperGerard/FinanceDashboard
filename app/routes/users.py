from flask import Blueprint, render_template,redirect,request
from flask_login import login_required ,LoginManager,current_user
from ..forms.form import FormularioInicio,FormularioRegistro
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
        
    