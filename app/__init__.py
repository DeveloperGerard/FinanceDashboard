from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_login import LoginManager 
from config import Config 
 
db = SQLAlchemy() 
login_manager = LoginManager() 
 
def create_app(): 
    app = Flask(__name__) 
    app.config.from_object(Config) 
 
    db.init_app(app) 
    login_manager.init_app(app) 
    login_manager.login_view = 'auth.login' 
    
    @login_manager.user_loader
    def load_user(user_id):
        return Usuario.obtener_por_id(int(user_id))
    return app 
