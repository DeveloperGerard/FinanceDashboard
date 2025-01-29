"""
Archivo despliegue
"""
from app import create_app
from app.routes.user import user
from app.routes.user_functions import user_functions
from app.routes.public import public
from flask_mail import Mail,Message
app = create_app()
app.register_blueprint(user)
app.register_blueprint(user_functions)
app.register_blueprint(public)

app.config['MAIL_SERVER']='smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = 'dashboardfinance1@gmail.com'
app.config['MAIL_PASSWORD'] = 'vtow xsqo qico odwj'
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
mail = Mail(app)

if __name__=="__main__":
    app.debug=True 
    app.run()