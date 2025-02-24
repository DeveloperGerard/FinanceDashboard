"""
Archivo despliegue
"""

from app import create_app
from app.routes.auth import auth
from app.routes.user_functions import user_functions
from app.routes.public import public
from flask_mail import Mail
app = create_app()#aplicacion


#registramos los blueprint
#?Informacion acerca de los blueprint:https://juncotic.com/blueprints-en-flask/

app.register_blueprint(auth) #mostrar informacion de usuario
app.register_blueprint(user_functions) #funciones del usuario
app.register_blueprint(public) #informacion/Funciones publicas

mail = Mail(app) #objeto Mail para manejo de mensajes de correo

if __name__=="__main__":
    app.debug=True 
    app.run()