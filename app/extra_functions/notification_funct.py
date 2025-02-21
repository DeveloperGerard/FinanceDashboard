"""
    Funciones de notificacion
"""

from flask_login import current_user
from flask import render_template
from flask_mail import Message
from app.models.importaciones import User,Email_message
from flask_apscheduler import APScheduler
import random
scheduler = APScheduler()

def send_gmail_confirmation(token):
    """
        Envia la plantilla para confirmar tu correo con el `token` de seguridad
        a tu correo.
    """

    from server import mail
    user    = User().get_by_id(current_user.id)
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[current_user.email],subject="Confirmacion de correo")
    username = user.username
    title = f"Confirma tu correo {username}" 
    message.html = render_template("extra_functions/mailconfirmation.html",title=title,token=token)
    mail.send(message)
    return "Enviado"
  
def send_gmail(recipient):
    """
        Envia un mensaje de `bienvenida` a tu correo.
    """

    from server import mail
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[recipient])
    user    = User().get_by_id(current_user.id)
    username = user.username
    title = f"Gracias por tu registro {username}😊" 
    body  = """Bienvenido a esta comunidad ahora ya puedes disfrutar de nuestras herramientas
            si tienes dudas puedes dirigirte al que esta en nuestra pagina tutorial para aprender a usar la web y gestionar tus 
            finanzas.
    """
    message.html = render_template("extra_functions/mail.html",title=title,body=body)
    mail.send(message)
    return "Enviado"

def daily_email():
    """
        Envia un mensaje diariamente todos los dias a las `9:00 de la mañana` a tu correo el mensaje es `aleatorio`.
    """
    from server import app
    with app.app_context():
        #Importaciones necesarias
        from server import mail
        from flask_mail import Message

        #receptores
        users = User().get_all()

        #objeto mensaje
        message = Message(sender="dashboardfinance1@gmail.com",recipients=[user.email for user in users],subject="Mensaje informativo")

        #mensajes disponibles
        messages = Email_message().get_all()

        #eligiendo el mensaje aleatorio
        message_elected = (messages[random.randint(0,1)]).template_name

        #añadiendo html al mensaje
        message.html = render_template(f"extra_functions/messages_dialy/{message_elected}")

        #envio
        mail.send(message)
        scheduler.remove_job("hola")
scheduler.add_job(id="hola",func=daily_email,trigger="cron",hour=15,minute=20)
scheduler.start()