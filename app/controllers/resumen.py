from flask_login import current_user
from datetime import datetime, timedelta
from sqlalchemy import func
from app.models.importaciones import Income, Service, Loan, Account
from app import db  # Add this import

def get_financial_summary(user_id):
    # Aquí iría la lógica para calcular el resumen financiero
    total_income = Income.query.filter_by(user_id=user_id).with_entities(db.func.sum(Income.amount)).scalar()
    total_services = Service.query.filter_by(user_id=user_id).with_entities(db.func.sum(Service.price)).scalar()
    total_loans = Loan.query.filter_by(user_id=user_id).with_entities(db.func.sum(Loan.remaining_price)).scalar()
    total_balance = Account.query.filter_by(user_id=user_id).with_entities(db.func.sum(Account.balance)).scalar()

    # Calcular el balance final
    final_balance = total_income - total_services - total_loans + total_balance

    return {
        'total_income': total_income or 0,
        'total_services': total_services or 0,
        'total_loans': total_loans or 0,
        'total_balance': total_balance or 0,
        'final_balance': final_balance
    }