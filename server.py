"""
Archivo despliegue
"""
from app import create_app
from app.routes.main import main
app = create_app()
app.register_blueprint(main)
#a

if __name__=="__main__":
    app.debug=True 
    app.run()