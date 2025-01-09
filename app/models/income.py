from app import db

class Income(db.Model):
    __tablename__ = "incomes"
    id            = db.Column(db.Integer,primary_key=True)
    income_name   = db.Column(db.String(50),nullable=False)
    date          = db.Column(db.DateTime(),nullable=False)
    amount        = db.Column(db.Integer,nullable=False)
    user_id       = db.Column(db.Integer,db.ForeignKey("users.id"))
    user          = db.relationship("User",back_populates="incomes")