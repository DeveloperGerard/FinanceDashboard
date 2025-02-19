from ..models.loan_payment import  Loan_payment
from app import db

class LoanPaymentController:
    """
        Controlador de `Pago de prestamos`.

        Permite realizar las funciones basicas(`borrar,actualizar,crear objetos`) del modelo pago de prestamos.
    """

    @staticmethod
    def create_loan_payment(amount,date,description,loan_id,user_id):
        loan_payment              = Loan_payment()
        loan_payment.amount       = amount
        loan_payment.date         = date
        loan_payment.description  = description
        loan_payment.loan_id      = loan_id
        loan_payment.user_id      = user_id
        db.session.add(loan_payment)
        db.session.commit()
        return loan_payment
    
    @staticmethod
    def delete_loan_payment(loan_payment:object):
        db.session.delete(loan_payment)
        db.session.commit()
        return  loan_payment
    
    @staticmethod
    def update_loan_payment(loan_payment:object):
        db.session.add(loan_payment)
        db.session.commit()

        