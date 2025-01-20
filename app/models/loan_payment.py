from app import db 

class Loan_payment(db.Model):
    __tablename__ = "loan_payments"

    #columnas
    id          = db.Column(db.Integer,primary_key=True)
    amount      = db.Column(db.Integer,nullable=False)
    date        = db.Column(db.DateTime(),nullable=False)
    description = db.Column(db.Text(),nullable=True)
    loan_id     = db.Column(db.Integer,db.ForeignKey("loans.id",ondelete="CASCADE"))
    
    #relaciones
    loan        = db.relationship("Loan",back_populates="loan_payments")
    
    #Funciones para obtener datos del model 'pago de prestamos'
    @staticmethod 
    def get_all_by_loanid(id:int):
        all_loanpayments = db.session.execute(db.select(Loan_payment)).scalars()
        all_loanpayments_list =[]
        for payment in all_loanpayments:
            if payment.loan_id == id:
                all_loanpayments_list.append(payment)
        return all_loanpayments_list
    

    

