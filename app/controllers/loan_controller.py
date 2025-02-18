from ..models.loan import Loan
from app import db

class LoanController:
    @staticmethod
    def create_loan(name,holder,price,quota,user_id,account_id,reamingin_price,tea=0,tea_mora=0):
        loan                 = Loan()
        loan.loan_name       = name
        loan.holder          = holder
        loan.price           = price
        loan.quota           = quota
        loan.tea             = tea
        loan.tea_mora        = tea_mora
        loan.user_id         = user_id
        loan.account_id      = account_id
        loan.reamining_price = reamingin_price
        db.session.add(loan)
        db.session.commit()
        return loan
    
    @staticmethod
    def delete_loan(loan_id):
        try:
            loan = Loan.query.get(loan_id)
            if loan:
                db.session.delete(loan)
                db.session.commit()
                return True
            return False
        except Exception as e:
            print(f"Delete loan error: {str(e)}")
            db.session.rollback()
            return False
        
    @staticmethod
    def update_loan(loan:object):
        db.session.add(loan)
        db.session.commit()