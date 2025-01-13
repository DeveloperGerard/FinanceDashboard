"""
Archivo despliegue
"""
from app import create_app
from app.routes.users import main
app = create_app()
app.register_blueprint(main)


if __name__=="__main__":
    app.debug=True 
    app.run()