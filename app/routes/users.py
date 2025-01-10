from flask import Blueprint, render_template,redirect
from flask_login import login_required ,LoginManager,current_user

main= Blueprint('main', __name__) 

@main.route('/') 
@main.route('/index') 
def index(): 
    if current_user.is_authenticated:
        return redirect('/home')
    else:
        return render_template("index.html")
    

