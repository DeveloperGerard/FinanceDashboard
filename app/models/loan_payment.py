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