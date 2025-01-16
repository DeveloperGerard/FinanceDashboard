from app import db 

class Loan(db.Model):
    __tablename__   = "loans"
<<<<<<< HEAD
=======

    #columnas
>>>>>>> origin/ramaprueba
    id              = db.Column(db.Integer,primary_key=True)
    loan_name       = db.Column(db.String(50),nullable=False)
    holder          = db.Column(db.String(50),nullable=False)
    price           = db.Column(db.Integer,nullable=False)
    quota           = db.Column(db.Integer,nullable=True)
    tea             = db.Column(db.Integer,nullable=True)
    tea_mora        = db.Column(db.Integer,nullable=True)
    reamining_price = db.Column(db.Integer,nullable=False)
    user_id         = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
<<<<<<< HEAD
    user            = db.relationship("User",back_populates="loans")     
    account_id      = db.Column(db.Integer,db.ForeignKey("accounts.id",ondelete="CASCADE"))
    account         = db.relationship("Account",back_populates="accounts")            
=======
    account_id      = db.Column(db.Integer,db.ForeignKey("accounts.id",ondelete="CASCADE"))

    #relaciones
    user            = db.relationship("User",back_populates="loans")     
    account         = db.relationship("Account",back_populates="accounts")            

    #Funciones para obtener datos del modelo prestamo

    @staticmethod
    def get_all_by_userid(id:int):
        all_loans = db.session.execute(db.select(Loan)).scalars()
        all_loans_list =[]
        for loan in all_loans:
            if loan.user_id ==id:
                all_loans_list.append(loan)
        return all_loans_list
    @staticmethod 
    def get_full_amount():
        all_loans = db.session.execute(db.select(Loan)).scalars()
        amount = 0
        for loan in all_loans:
            amount+= loan.price
        return amount
    @staticmethod 
    def get_full_reamining_amount():
        all_loans = db.session.execute(db.select(Loan)).scalars()
        amount = 0
        for loan in all_loans:
            amount += loan.reamining_price
        return amount
    
>>>>>>> origin/ramaprueba
