"""
    Funciones para que un usuario confirme su correo.
"""

from itsdangerous import URLSafeTimedSerializer

#?Informacion de serializacion:https://www.vpnunlimited.com/es/help/cybersecurity/serialization

def genera_token(email):
    """
        A partir de la cadena gmail y  PASSWORD_SALT genera un `token`.
    """
    from server import app
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])#Inicializamos la clase URLSafeTimedSerializer con la SECRET_KEY variable de configuracion
    return serializer.dumps(email,salt=app.config["SECURITY_PASSWORD_SALT"])

def confirm_token(token,expiration=3600):
    """
    Verifica que el token `email encriptado` sea igual al email del usuario para confirmar el correo.
    """
    from server import app
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    try:
        email = serializer.loads(
            token,salt=app.config["SECURITY_PASSWORD_SALT"],max_age=expiration
        )
        return email
    except Exception:
        return False



