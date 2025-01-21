from ..models.service_payment import  Service_payment
from app import db

class ServicePaymentController:
    @staticmethod
    def create_service_payment(amount,date,description,service_id):
        service_payment              = Service_payment()
        service_payment.amount       = amount
        service_payment.date         = date
        service_payment.description  = description
        service_payment.service_id   = service_id
        db.session.add(service_payment)
        db.session.commit()
        return service_payment
    
    @staticmethod
    def delete_service_payment(service_payment:object):
        db.session.delete(service_payment)
        db.session.commit()
        return  service_payment
    
    @staticmethod
    def update_service_payment(service_payment:object):
        db.session.add(service_payment)
        db.session.commit()

        