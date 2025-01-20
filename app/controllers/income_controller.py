from ..models.income import  Income
from app import db

class IncomeController:
    @staticmethod
    def create_income(name,date,amount):
        ingreso             = Income()
        ingreso.income_name = name
        ingreso.date        = date
        ingreso.amount      = amount
        db.session.add(ingreso)
        db.session.commit()
        return ingreso
    
    @staticmethod
    def delete_income(income:object):
        db.session.delete(income)
        db.session.commit()
        return  income
    
    @staticmethod
    def update_income(income:object):
        db.session.add(income)
        db.session.commit()

        