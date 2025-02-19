from ..models.scheduled_incomes import Scheduled_income 
from app import db

class IncomeController:
    """
        Controlador de `Ingresos programados`.

        Permite realizar las funciones basicas(`borrar,actualizar,crear objetos`) del modelo ingresos programados.
    """

    @staticmethod
    def create_income(name,date,amount,user_id,description,next_income,pending_amount,categoria):
        income                = Scheduled_income()
        income.income_name    = name
        income.income_date    = date
        income.amount         = amount
        income.description    = description
        income.next_income    = next_income
        income.pending_amount = pending_amount
        income.category       = categoria
        income.user_id        = user_id
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

        