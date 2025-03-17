from ..models.income import  Income
from app import db

class IncomeController:
    """
        Controlador de `Ingresos`.

        Permite realizar las funciones basicas(`borrar,actualizar,crear objetos`) del modelo ingresos.
    """

    @staticmethod
    def create_income(name,date,amount,user_id,description,categoria,account_id):
        income                = Income()
        income.income_name    = name
        income.income_date    = date
        income.amount         = amount
        income.description    = description
        income.category       = categoria
        income.user_id        = user_id
        income.account_id     = account_id
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

        