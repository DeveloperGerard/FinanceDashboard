from app import db

class Service(db.Model):
    __tablename__   = "services"

    #columnas
    id               = db.Column(db.Integer,primary_key=True)
    service_name     = db.Column(db.String(50),nullable=False)
    description      = db.Column(db.String(100),nullable=True)
    date             = db.Column(db.Date(),nullable=False)
    category         = db.Column(db.String(45),nullable=False)
    price            = db.Column(db.Integer,nullable=False)
    reamining_price  = db.Column(db.Integer,nullable=False)
    user_id          = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    
    #relaciones
    service_payments = db.relationship("Service_payment",back_populates="service")
    user             = db.relationship("User",back_populates="services")

    #Funciones para obtener datos del modelo servicio
    @staticmethod
    def get_all_by_userid(id:int):
        all_services =db.session.execute(db.select(Service)).scalars()
        all_services_list =[]

        for service in all_services:
            if service.user_id == id:
                all_services_list.append(service)
        return all_services_list
    
    @staticmethod
    def get_all_by_category(category:str):
        all_services = db.session.execute(db.select(Service)).scalars()
        all_services_list=[]

        for service in all_services:
            if service.category==category:
                all_services_list.append(service)
        return all_services_list
    @staticmethod
    def get_full_amount():
        all_service = db.session.execute(db.select(Service)).scalars()
        amount = 0
        for service in all_service:
            amount += service.price
        return amount

