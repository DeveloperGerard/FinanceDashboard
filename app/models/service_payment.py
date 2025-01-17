from app import db 

class Service_payment(db.Model):
    __tablename__ = "service_payments"

    #columnas
    id          = db.Column(db.Integer,primary_key=True)
    amount      = db.Column(db.Integer,nullable=False)
    date        = db.Column(db.DateTime(),nullable=False)
    description = db.Column(db.Text(),nullable=True)
    service_id  = db.Column(db.Integer,db.ForeignKey("services.id",ondelete="CASCADE"))

    #relaciones
    service     = db.relationship("Service",back_populates="service_payments")
