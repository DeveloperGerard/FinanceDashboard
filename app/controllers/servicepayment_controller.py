from ..models.service_payment import  Service_payment
from app import db

class ServicePaymentController:
    """
        Controlador de `Pago de servicios`.

        Permite realizar las funciones basicas(`borrar,actualizar,crear objetos`) del modelo pago de servicios.
    """

    @staticmethod
    def create_service_payment(amount,date,description,service_id,user_id):
        service_payment              = Service_payment()
        service_payment.amount       = amount
        service_payment.date         = date
        service_payment.description  = description
        service_payment.service_id   = service_id
        service_payment.user_id      = user_id
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

        