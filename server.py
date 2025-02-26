"""
Archivo despliegue
"""

from app import create_app
from app.routes.auth import auth
from app.routes.update_functions import update_functions
from app.routes.create_functions import create_functions
from app.routes.extra_functions import extra_functions
from app.routes.public import public
from flask_mail import Mail

app = create_app()#aplicacion


#registramos los blueprint
#?Informacion acerca de los blueprint:https://juncotic.com/blueprints-en-flask/

app.register_blueprint(auth) #mostrar informacion de usuario
app.register_blueprint(update_functions) #funciones para actualizar datos
app.register_blueprint(create_functions) #funciones para crear datos
app.register_blueprint(extra_functions) # funciones adicionales
app.register_blueprint(public,url_prefix="/public") #informacion/Funciones publicas
#! subdomain

mail = Mail(app) #objeto Mail para manejo de mensajes de correo

if __name__=="__main__":
    app.debug=True 
    app.run()