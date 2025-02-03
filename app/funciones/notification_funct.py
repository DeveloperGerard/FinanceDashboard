from flask_login import current_user
from flask import render_template
from flask_mail import Message
from app.models.importaciones import User
from flask_apscheduler import APScheduler
scheduler = APScheduler()

def send_gmail_confirmation(token):
    from server import mail
    user    = User().get_by_id(current_user.id)
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[current_user.email])
    username = user.username
    title = f"Confirma tu correo{username}" 
    message.html = render_template("public/mailconfirmation.html",title=title,token=token)
    mail.send(message)
    return "Enviado"
  
def send_gmail(recipient):
    from server import mail
    message = Message(sender="dashboardfinance1@gmail.com",recipients=[recipient])
    user    = User().get_by_id(current_user.id)
    username = user.username
    title = f"Gracias por tu registro {username}😊" 
    body  = """Bienvenido a esta comunidad ahora ya puedes disfrutar de nuestras herramientas
            si tienes dudas puedes dirigirte al que esta en nuestra pagina tutorial para aprender a usar la web y gestionar tus 
            finanzas.
    """
    message.html = render_template("public/mail.html",title=title,body=body)
    mail.send(message)
    return "Enviado"

def daily_email():
    from server import app
    with app.app_context():
        from server import mail,Message
        users = User().get_all()
        message = Message(sender="dashboardfinance1@gmail.com",recipients=[user.email for user in users])
        title = f"Acuerdate de pagar tus prestamos😊" 
        body  = """
            Un préstamo es una transacción financiera en la que una parte, denominada prestamista, proporciona una cantidad
            específica de dinero o recursos a otra parte, 
            conocida como prestatario, con la expectativa de que se devuelva en el futuro, generalmente con intereses.
        """
        message.html = render_template("public/mail.html",title=title,body=body)
        mail.send(message)
scheduler.add_job(id="hola",func=daily_email,trigger="cron",hour=16,minute=4)
scheduler.start()
