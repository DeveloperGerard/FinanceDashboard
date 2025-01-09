import os 
from dotenv import load_dotenv 
 
load_dotenv() 
 
class Config: 
    SECRET_KEY = "adlasdlalsdlasdlel"
    SQLALCHEMY_DATABASE_URI ="mysql://root@localhost/finance"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
