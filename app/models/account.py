from app import db 

class Account(db.model):
    __tablename__ = "accounts"
    id            = db.Column(db.Integer,primary_key=True)
    account_name  = db.Column(db.String(50),nullable=False)
    type          = db.Column(db.String(50),nullable=False)
    user_id       = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    user          = db.relationship("User",back_populates="accounts")
    accounts      = db.relationship("Loan",back_populates="account")