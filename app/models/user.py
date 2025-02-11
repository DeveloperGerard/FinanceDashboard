from app import db 
from werkzeug.security import generate_password_hash, check_password_hash 
from flask_login import UserMixin 

class User(UserMixin, db.Model): 
    __tablename__  = "users"

    #columnas
    id             = db.Column(db.Integer, primary_key=True) 
    username       = db.Column(db.String(64), unique=True, nullable=False) 
    email          = db.Column(db.String(120), unique=True, nullable=False) 
    password_hash  = db.Column(db.String(255)) 
    balance        = db.Column(db.Integer)
    email_conf     = db.Column(db.Boolean(),default=False)
    
    #relaciones
    incomes        = db.relationship("Income",back_populates="user")
    services       = db.relationship("Service",back_populates="user")
    services_pay   = db.relationship("Service_payment",back_populates="user")
    accounts       = db.relationship("Account",back_populates="user")
    loans          = db.relationship("Loan",back_populates="user")
    loans_pay      = db.relationship("Loan_payment",back_populates="user")

    def set_password(self, password): 
        self.password_hash = generate_password_hash(password) 

    def check_password(self, password): 
        return check_password_hash(self.password_hash, password)
     
    #Funciones para obtener datos del modelo usuario

    @staticmethod 
    def get_all():
        all_users = db.session.execute(db.select(User)).scalars()
        all_users_list = []
        for user in all_users:
            all_users_list.append(user)
        return(all_users_list)

    @staticmethod
    def get_by_id(id):
        user = User.query.filter_by(id=id).first()
        return user
    
    @staticmethod 
    def get_by_email(email):
        user = User.query.filter_by(email=email).first()
        return user
    @staticmethod 
    def get_by_name(username):
        user = User.query.filter_by(username=username).first()
        return user
        
        