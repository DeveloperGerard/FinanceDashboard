from ..models.income import  Income
from app import db

class IncomeController:
    @staticmethod
    def create_income(name,date,amount,user_id):
        income             = Income()
        income.income_name = name
        income.date        = date
        income.amount      = amount
        income.user_id     = user_id
        db.session.add(income)
        db.session.commit()
        return income
    
    @staticmethod
    def delete_income(income:object):
        db.session.delete(income)
        db.session.commit()
        return  income
    
    @staticmethod
    def update_income(income:object):
        db.session.add(income)
        db.session.commit()

        