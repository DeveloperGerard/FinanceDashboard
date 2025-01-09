from app import db

class Service(db.model):
    __tablename__   = "services"
    id              = db.Column(db.Integer,primary_key=True)
    service_name    = db.Column(db.String(50),nullable=False)
    description     = db.Column(db.String(100),nullable=True)
    date            = db.Column(db.Date(),nullable=False)
    category        = db.Column(db.String(45),nullable=False)
    price           = db.Column(db.Integer,nullable=False)
    reamining_price = db.Column(db.Integer,nullable=False)
    user_id         = db.Column(db.Integer,db.ForeingKey("users.id",ondelete="CASCADE"))
    user            = db.relationship("User",back_populates="services")
