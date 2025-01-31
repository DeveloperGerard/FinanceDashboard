import os 
from dotenv import load_dotenv 
 
load_dotenv() 
 
class Config: 
    SECRET_KEY = "adlasdlalsdlasdlel"
    SQLALCHEMY_DATABASE_URI ="mysql://root@localhost/finance"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    MAIL_SERVER='smtp.gmail.com'
    MAIL_PORT  = 465
    MAIL_USERNAME = 'dashboardfinance1@gmail.com'
    MAIL_PASSWORD = 'vtow xsqo qico odwj'
    MAIL_USE_TLS = False
    MAIL_USE_SSL = True

