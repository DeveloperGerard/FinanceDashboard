from flask_login import current_user
from datetime import datetime, timedelta
from sqlalchemy import func
from app.models.importaciones import Income, Service, Loan, Account
from app import db  # Add this import

def get_financial_summary(user_id):
    total_balance = db.session.query(func.sum(Account.balance)).filter_by(user_id=user_id).scalar() or 0
    total_income = db.session.query(func.sum(Income.amount)).filter_by(user_id=user_id).scalar() or 0
    total_services = db.session.query(func.sum(Service.price)).filter_by(user_id=user_id).scalar() or 0
    total_loans = db.session.query(func.sum(Loan.reamining_price)).filter_by(user_id=user_id).scalar() or 0  

    # Convertir todo a float para evitar problemas con decimal.Decimal
    total_balance = float(total_balance)
    total_income = float(total_income)
    total_services = float(total_services)
    total_loans = float(total_loans)

    final_balance = total_balance + total_income - total_services - total_loans

    return {
        'total_balance': total_balance,
        'total_income': total_income,
        'total_services': total_services,
        'total_loans': total_loans,
        'final_balance': final_balance
    }