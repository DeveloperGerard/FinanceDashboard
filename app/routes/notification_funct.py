from flask_login import current_user
from flask import render_template
from flask_mail import Message
from app.models.importaciones import User


def send_gmail_form():
    from server import mail
    user    = User().get_by_id(current_user.id)
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[current_user.email])
    username = user.username
    title = f"Confirma tu correo{username}" 
    message.html = render_template("public/mailform.html",title=title)
    mail.send(message)
    return "Enviado"