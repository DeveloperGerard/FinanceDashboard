"""
This module updates the password of a user in the database.
"""

from app import create_app, db  # Importa tu aplicación y la base de datos
from app.models.user import User  # Importa el modelo User

app = create_app()

with app.app_context():
    user = User.query.filter_by(email="rauquematias601@gmail.com").first()
    if user:
        user.set_password("matiasrauque1")  # Guarda de nuevo con pbkdf2
        db.session.commit()
        print("Contraseña actualizada con pbkdf2:sha256")
    else:
        print("Usuario no encontrado.")