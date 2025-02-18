import os 
from dotenv import load_dotenv 
 
load_dotenv() 
 
class Config: 
    SECRET_KEY = os.environ.get('12345') or '12345' 
    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root@localhost/finance_dashboard'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
