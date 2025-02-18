from ..models.service import  Service
from app import db
from datetime import datetime

class ServiceController:
    @staticmethod
    def create_service(service_name, description, date, category, price, user_id):
        service = Service()
        service.service_name = service_name
        service.description = description
        service.date = date
        service.category = category
        service.price = price
        service.remaining_price = price
        service.user_id = user_id

        # Si la fecha del servicio es la fecha actual, restamos del balance
        if date <= datetime.now().date():  # Compara con la fecha actual
            user = User.query.get(user_id)
            if user:
                user.balance -= price  # Restamos el precio del servicio del balance

        db.session.add(service)
        db.session.commit()
        return service
    
    @staticmethod
    def delete_service(service:object):
        db.session.delete(service)
        db.session.commit()
        return  service
    
    @staticmethod
    def update_service(service:object):
        db.session.add(service)
        db.session.commit()