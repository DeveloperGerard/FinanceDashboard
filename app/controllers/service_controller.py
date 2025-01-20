from ..models.service import  Service
from app import db

class ServiceController:
    @staticmethod
    def create_service(name,description,date,category,user_id,price,reamingin_price):
        servicio                 = Service()
        servicio.name            = name
        servicio.description     = description
        servicio.date            = date
        servicio.category        = category
        servicio.user_id         = user_id
        servicio.reamining_price = reamingin_price
        servicio.price           = price 
        db.session.add(servicio)
        db.session.commit()
        return servicio
    
    @staticmethod
    def delete_service(service:object):
        db.session.delete(service)
        db.session.commit()
        return  service
    
    @staticmethod
    def update_service(service:object):
        db.session.add(service)
        db.session.commit()