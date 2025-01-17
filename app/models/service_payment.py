from app import db 

class Loan_payment(db.Model):
    __tablename__ = "service_payments"

    #columnas
    id     = db.Column(db.Integer,primary_key=True)
    amount = db.Column(db.Integer,nullable=False)
    date   = db.Column(db.Datetime(),nullable=False)
    description = db.Column(db.Text(),nullable=True)