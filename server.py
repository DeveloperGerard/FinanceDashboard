"""
Archivo despliegue
"""
from flask_wtf import CSRFProtect
from flask_wtf.csrf import generate_csrf
from app import create_app
from app.routes.user import user
from app.routes.user_functions import user_functions
from app.routes.public import public

app = create_app()
csrf = CSRFProtect(app)

app.register_blueprint(user)
app.register_blueprint(user_functions)
app.register_blueprint(public)

@app.context_processor
def inject_csrf_token():
    return dict(csrf_token=generate_csrf())

if __name__ == "__main__":
    app.debug = True
    app.run()