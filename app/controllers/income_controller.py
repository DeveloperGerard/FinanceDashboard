from ..models.income import  Income
from app import db
from datetime import datetime

class IncomeController:
    @staticmethod
    def create_income(name, date, amount, user_id):
        income = Income()
        income.income_name = name
        income.date = date
        income.amount = amount
        income.user_id = user_id

        # Si la fecha del ingreso es la fecha actual, sumamos al balance
        if date <= datetime.now().date():  # Compara con la fecha actual
            user = User.query.get(user_id)
            if user:
                user.balance += amount  # Se suma al balance si la fecha es hoy o pasada

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

        