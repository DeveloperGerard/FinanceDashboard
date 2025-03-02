"""
Archivo de configuracion:\n
-mail \n
-base de datos\n
-etc\n
"""


import os 
from dotenv import load_dotenv 
 
load_dotenv() 
 
class Config: 
    SECRET_KEY = "adlasdlalsdlasdlel"
    SQLALCHEMY_DATABASE_URI ="mysql://root@localhost/finance_dashboard"
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    #MAIL CONFIG
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT  = 465
    MAIL_USERNAME = 'dashboardfinance1@gmail.com'
    MAIL_PASSWORD = 'vtow xsqo qico odwj'
    
    #*protocolos de criptografia para encriptar la informacion al ser enviada 
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

    #MAIL VALIDATION(TOKEN)
    SECURITY_PASSWORD_SALT = "3as3#Pas21zz3A$532" 

    """
    salt password:Tecnica de criptografia que añade cadena de caracteres aleatorios antes de aplicar una funcion hash
    """