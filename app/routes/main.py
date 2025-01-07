from flask import Blueprint, render_template 
from flask_login import login_required ,LoginManager

main= Blueprint('main', __name__) 

@main.route('/') 
@main.route('/index') 
def index(): 
    return render_template('index.html') 
