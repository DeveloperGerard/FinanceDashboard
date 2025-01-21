from ..models.account import  Account
from app import db

class AccountController:
    @staticmethod
    def create_account(name,card):
        cuenta              = Account()
        cuenta.account_name = name
        cuenta.card         = card
        db.session.add(Account)
        db.session.commit()
        return cuenta
    
    @staticmethod
    def delete_account(account:object):
        db.session.delete(Account)
        db.session.commit()
        return  account
    
    @staticmethod
    def update_account(account:object):
        db.session.add(account)
        db.session.commit()

        
