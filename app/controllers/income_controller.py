from ..models.income import  Income
from app import db

class IncomeController:
    @staticmethod
    def create_Income(name,type):
        cuenta              = Income()
        cuenta.Income_name = name
        cuenta.type         = type
        db.session.add(Income)
        db.session.commit()
        return cuenta
    
    @staticmethod
    def delete_Income(income:object):
        db.session.delete(income)
        db.session.commit()
        return  income
    
    @staticmethod
    def update_Income(income:object):
        db.session.add(income)
        db.session.commit()

        