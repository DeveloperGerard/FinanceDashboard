"""
Archivo despliegue
"""
from app import create_app
from app.routes.user import user
from app.routes.user_functions import user_functions
from app.routes.public import public
from flask_mail import Mail
app = create_app()
app.register_blueprint(user)
app.register_blueprint(user_functions)
app.register_blueprint(public)

mail = Mail(app)

if __name__=="__main__":
    app.debug=True 
    app.run()