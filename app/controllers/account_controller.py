from ..models.account import  Account
from app import db

class AccountController:
    @staticmethod
    def create_account(name,card,user_id):
        account              = Account()
        account.account_name = name
        account.card         = card
        account.user_id      = user_id
        db.session.add(account)
        db.session.commit()
        return account
    
    @staticmethod
    def delete_account(account:object):
        db.session.delete(account)
        db.session.commit()
        return  account
    
    @staticmethod
    def update_account(account:object):
        db.session.add(account)
        db.session.commit()

        
