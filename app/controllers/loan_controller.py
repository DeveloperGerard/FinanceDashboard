from ..models.loan import Loan
from app import db

class LoanController:
    @staticmethod
    def create_loan(name,holder,price,quota,user_id,account_id,reamingin_price,tea=0,tea_mora=0):
        prestamo                 = Loan()
        prestamo.name            = name
        prestamo.holder          = holder
        prestamo.price           = price
        prestamo.quota           = quota
        prestamo.tea             = tea
        prestamo.tea_mora        = tea_mora
        prestamo.user_id         = user_id
        prestamo.account_id      = account_id
        prestamo.reamining_price = reamingin_price
        db.session.add(prestamo)
        db.session.commit()
        return prestamo
    
    @staticmethod
    def delete_loan(prestamo:object):
        db.session.delete(prestamo)
        db.session.commit()
        return  prestamo
    
    @staticmethod
    def update_loan(prestamo:object):
        db.session.add(prestamo)
        db.session.commit()