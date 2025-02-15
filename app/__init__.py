from flask import Flask 
from flask_sqlalchemy import SQLAlchemy 
from flask_migrate import Migrate
from flask_login import LoginManager 
from config import Config 
 
db = SQLAlchemy() 
login_manager = LoginManager() 
 
def create_app(): 
    app = Flask(__name__) 
    app.config.from_object(Config) 
    db.init_app(app) 
    login_manager.init_app(app) 
    login_manager.login_view = 'auth' 
    Migrate(app,db)
    from app.models import user,account,income,loan,service,service_payment,loan_payment
    @login_manager.user_loader
    def load_user(user_id):
        return user.User().get_by_id(int(user_id))
    return app 
