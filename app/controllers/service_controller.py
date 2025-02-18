from ..models.service import  Service
from app import db

class ServiceController:
    @staticmethod
    def create_service(name,description,date,category,user_id,price,reamingin_price):
        service                 = Service()
        service.service_name    = name
        service.description     = description
        service.date            = date
        service.category        = category
        service.user_id         = user_id
        service.reamining_price = reamingin_price
        service.price           = price 
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