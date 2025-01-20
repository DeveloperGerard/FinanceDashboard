from ..models.service_payment import  Service_payment
from app import db

class ServicePaymentController:
    @staticmethod
    def create_service_payment(amount,date,description,service_id):
        servicio_pagado              = Service_payment()
        servicio_pagado.amount       = amount
        servicio_pagado.date         = date
        servicio_pagado.description  = description
        servicio_pagado.service_id   = service_id
        db.session.add(servicio_pagado)
        db.session.commit()
        return servicio_pagado
    
    @staticmethod
    def delete_service_payment(service_payment:object):
        db.session.delete(service_payment)
        db.session.commit()
        return  service_payment
    
    @staticmethod
    def update_service_payment(service_payment:object):
        db.session.add(service_payment)
        db.session.commit()

        