from app import db 

class Loan(db.Model):
    __tablename__   = "loans"
    id              = db.Column(db.Integer,primary_key=True)
    loan_name       = db.Column(db.String(50),nullable=False)
    holder          = db.Column(db.String(50),nullable=False)
    price           = db.Column(db.Integer,nullable=False)
    quota           = db.Column(db.Integer,nullable=True)
    tea             = db.Column(db.Integer,nullable=True)
    tea_mora        = db.Column(db.Integer,nullable=True)
    reamining_price = db.Column(db.Integer,nullable=False)
    user_id         = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    user            = db.relationship("User",back_populates="loans")     
    account_id      = db.Column(db.Integer,db.ForeignKey("accounts.id",ondelete="CASCADE"))
    account         = db.relationship("Account",back_populates="accounts")            