import os 
from dotenv import load_dotenv 
 
load_dotenv() 
 
class Config: 
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key' 
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///dev.db' 
    SQLALCHEMY_TRACK_MODIFICATIONS = False 
