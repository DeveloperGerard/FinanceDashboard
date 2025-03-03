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
    login_manager.login_view = 'user' 
    
    #-----Importando los modelos para la migracion
    Migrate(app,db)
    from app.models import user,account,income,loan,service,service_payment,loan_payment,emailmessage

    #-----Inicializando el manejo de sesiones(inicio,cierre)
    @login_manager.user_loader
    def load_user(user_id):
        return user.User().get_by_id(int(user_id))
    
    #-----Despues de cada solicitud enviamos una respuesta con esos 3 encabezados
    @app.after_request
    def add_header(response):
        
        #Las cabezeras/headers llevan informacion sobre el contenido de la peticion o sobre el servidor
        response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
        response.headers['Pragma'] = 'no-cache'
        response.headers['Expires'] = '0'

        #retornamos la respuesta con las cabezeras establecidas
        return response
    return app 