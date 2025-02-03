from itsdangerous import URLSafeTimedSerializer

#token functions

def genera_token(email):
    """
    A partir de la cadena gmail genera un token
    """
    from server import app
    serializer = URLSafeTimedSerializer(app.config["SECRET_KEY"])
    return serializer.dumps(email,salt=app.config["SECURITY_PASSWORD_SALT"])

def confirm_token(token,expiration=3600):
    """
    Verifica que el token(email encriptado) sea igual al email del usuario para confirmar el correo
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



