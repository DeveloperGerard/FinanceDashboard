from ..models.loan import Loan
from app import db

class LoanController:
    """
        Controlador de `Prestamos`.

        Permite realizar las funciones basicas(`borrar,actualizar,crear objetos`) del modelo prestamos.
    """

    @staticmethod
    def create_loan(name,holder,price,quota,user_id,account_id,reamingin_price,date,expiration_date,tea=0):
        loan                 = Loan()
        loan.loan_name       = name
        loan.holder          = holder
        loan.price           = price
        loan.quota           = quota
        loan.tea             = tea
        loan.user_id         = user_id
        loan.account_id      = account_id
        loan.reamining_price = reamingin_price
        loan.date            = date
        loan.expiration_date = expiration_date
        db.session.add(loan)
        db.session.commit()
        return loan
    
    @staticmethod
    def delete_loan(loan:object):
        db.session.delete(loan)
        db.session.commit()
        return  loan
    
    @staticmethod
    def update_loan(loan:object):
        db.session.add(loan)
        db.session.commit()