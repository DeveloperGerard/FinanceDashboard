from ..models.loan_payment import  Loan_payment
from app import db

class LoanPaymentController:
    @staticmethod
    def create_loan_payment(amount,date,description,loan_id):
        prestamo_pagado              = Loan_payment()
        prestamo_pagado.amount       = amount
        prestamo_pagado.date         = date
        prestamo_pagado.description  = description
        prestamo_pagado.loan_id      = loan_id
        db.session.add(prestamo_pagado)
        db.session.commit()
        return prestamo_pagado
    
    @staticmethod
    def delete_loan_payment(loan_payment:object):
        db.session.delete(loan_payment)
        db.session.commit()
        return  loan_payment
    
    @staticmethod
    def update_loan_payment(loan_payment:object):
        db.session.add(loan_payment)
        db.session.commit()

        