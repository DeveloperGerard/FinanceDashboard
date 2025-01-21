from app import db 

class Account(db.Model):
    __tablename__ = "accounts"
    id            = db.Column(db.Integer,primary_key=True)
    account_name  = db.Column(db.String(50),nullable=False)
    card          = db.Column(db.String(50),nullable=False)
    user_id       = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    user          = db.relationship("User",back_populates="accounts")
    accounts      = db.relationship("Loan",back_populates="account")
    @staticmethod 
    def get_all():
        all_accounts = db.session.execute(db.select(Account)).scalars()
        all_accounts_list = []
        for account in all_accounts:
            all_accounts_list.append(account)
        return(all_accounts_list)