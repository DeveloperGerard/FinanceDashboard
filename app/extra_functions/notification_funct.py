"""
    Funciones de notificacion
"""

from flask_login import current_user
from flask import render_template
from flask_mail import Message
from app.models.importaciones import User,Email_message
from flask_apscheduler import APScheduler
from app.forms.importaciones import FormularioCambiarContraseña,FormularioCambiarGmail
import random
scheduler = APScheduler()

def send_gmail_confirmation(token):
    """
        Envia la plantilla para confirmar tu correo con el `token` de seguridad
        a tu correo.
    """
    from server import mail

    #Obtenemos datos de el usuario para la plantilla
    user    = User().get_by_id(current_user.id)
    username = user.username

    #Creamos el objeto Message añadimos los atributos y sus valores que necesitamos y despues agregamos la plantilla que se mostrara en el email.
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[current_user.email],subject="Confirmacion de correo")
    message.html = render_template("extra_functions/mailconfirmation.html",username=username,token=token)

    #Enviamos al usuario el mensaje
    mail.send(message)
    return "Enviado"
def send_changepassword_request(token):
    from server import mail
    form = FormularioCambiarContraseña()
    #Obtenemos datos de el usuario para la plantilla
    user    = User().get_by_id(current_user.id)
    username = user.username

    #Creamos el objeto Message añadimos los atributos y sus valores que necesitamos y despues agregamos la plantilla que se mostrara en el email.
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[current_user.email],subject="Confirmacion de correo")
    message.html = render_template("extra_functions/change_password/mail_message.html",username=username,token=token,form=form)

    #Enviamos al usuario el mensaje
    mail.send(message)
    return "Enviado"

def send_changeemail_request(token):
    from server import mail
    form = FormularioCambiarGmail()
    #Obtenemos datos de el usuario para la plantilla
    user    = User().get_by_id(current_user.id)
    username = user.username

    #Creamos el objeto Message añadimos los atributos y sus valores que necesitamos y despues agregamos la plantilla que se mostrara en el email.
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[current_user.email],subject="Confirmacion de correo")
    message.html = render_template("extra_functions/change_email/mail_message.html",username=username,token=token,form=form)

    #Enviamos al usuario el mensaje
    mail.send(message)
    return "Enviado"

def send_gmail(recipient):
    """
        Envia un mensaje de `bienvenida` a tu correo.
    """
    from server import mail

    #Obtenemos datos de el usuario para la plantilla
    user    = User().get_by_id(current_user.id)
    username = user.username

    #Creamos el objeto Message añadimos los atributos y sus valores que necesitamos y despues agregamos la plantilla que se mostrara en el email.
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[recipient],subject="Bienvenido/a")
    message.html = render_template("extra_functions/mail.html",username=username)
    
    #Enviamos al usuario el mensaje 
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
        message_elected = (messages[random.randint(0,len(messages)-1)]).template_name

        #añadiendo html al mensaje
        message.html = render_template(f"extra_functions/messages_dialy/{message_elected}")

        #envio
        mail.send(message)
        scheduler.remove_job("hola")
scheduler.add_job(id="hola",func=daily_email,trigger="cron",hour=10,minute=12)
scheduler.start()