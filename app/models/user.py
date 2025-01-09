from app import db 
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin 
 
class User(UserMixin, db.Model): 
    __tablename__  = "users"
    id             = db.Column(db.Integer, primary_key=True) 
    username       = db.Column(db.String(64), unique=True, nullable=False) 
    email          = db.Column(db.String(120), unique=True, nullable=False) 
    password_hash  = db.Column(db.String(128)) 
    balance        = db.Column(db.Integer)
    def set_password(self, password): 
        self.password_hash = generate_password_hash(password) 
 
    def check_password(self, password): 
        return check_password_hash(self.password_hash, password) 
