from ..models.loan import Loan
from app import db
from datetime import datetime

class LoanController:

    @staticmethod
    def create_loan(loan_name, holder, price, quota, user_id, account_id, start_date):
        loan = Loan()
        loan.loan_name = loan_name
        loan.holder = holder
        loan.price = price
        loan.quota = quota
        loan.user_id = user_id
        loan.account_id = account_id
        loan.start_date = start_date

        # Si la fecha de inicio es la fecha actual o pasada, restamos del balance
        if start_date <= datetime.now().date():  # Compara con la fecha actual
            user = User.query.get(user_id)
            if user:
                user.balance -= price  # Restamos el precio del préstamo del balance

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