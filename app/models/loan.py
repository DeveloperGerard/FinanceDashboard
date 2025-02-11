from app import db 

class Loan(db.Model):
    __tablename__   = "loans"

    #columnas
    id              = db.Column(db.Integer,primary_key=True)
    loan_name       = db.Column(db.String(50),nullable=False)
    holder          = db.Column(db.String(50),nullable=False)
    price           = db.Column(db.Integer,nullable=False)
    date            = db.Column(db.Date(),nullable=False)
    quota           = db.Column(db.Integer,nullable=True)
    tea             = db.Column(db.Integer,nullable=True)
    tea_mora        = db.Column(db.Integer,nullable=True)
    reamining_price = db.Column(db.Integer,nullable=False)
    user_id         = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    account_id      = db.Column(db.Integer,db.ForeignKey("accounts.id",ondelete="CASCADE"))
    expiration_date = db.Column(db.Date(),nullable=False)
    #relaciones
    loan_payments   = db.relationship("Loan_payment",back_populates="loan") 
    user            = db.relationship("User",back_populates="loans")     
    account         = db.relationship("Account",back_populates="accounts_loan")            

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
    def get_all_for_payment(id:int):
        all_loans =db.session.execute(db.select(Loan)).scalars()
        all_loans_list =[]
        for loan in all_loans:
            if loan.user_id == id and loan.reamining_price>0:
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
    @staticmethod
    def get_by_id(id):
        loan =Loan.query.filter_by(id=id).first()
        return loan
    
    @staticmethod
    def get_loan_summary(id):
        all_loans        = db.session.execute(db.select(Loan)).scalars()
        all_amount       = 0
        payment_amount   = 0
        reamining_amount = 0
        progress         = 0
        for loan in all_loans:
            if loan.user_id ==id:
                all_amount += loan.price
                reamining_amount += loan.reamining_price
        payment_amount = all_amount - reamining_amount
        progress = (payment_amount*100)/all_amount
        return {"monto_total":all_amount,"monto_pagado":payment_amount,"monto_restante":reamining_amount,"progreso":progress}
