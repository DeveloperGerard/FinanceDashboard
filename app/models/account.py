from app import db 

class Account(db.Model):
    __tablename__ = "accounts"
    id            = db.Column(db.Integer,primary_key=True)
    account_name  = db.Column(db.String(50),nullable=False)
    card          = db.Column(db.String(50),nullable=False)
    user_id       = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    user          = db.relationship("User",back_populates="accounts")
    accounts      = db.relationship("Loan",back_populates="account")
    balance       = db.Column(db.Float, nullable=False)  # Add this attribute

    @staticmethod 
    def get_all_by_userid(id:int):
        all_account = db.session.execute(db.select(Account)).scalars()
        all_account_list =[]
        for account in all_account:
            if account.user_id ==id:
                all_account_list.append(account)
        return all_account_list

    def save(self):
        db.session.add(self)
        db.session.commit()