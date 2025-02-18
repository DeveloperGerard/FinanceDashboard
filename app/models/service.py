from app import db

class Service(db.Model):
    """
        Objeto que representa el modelo `Servicio`.

        Tiene las columnas con todos 
        datos necesarios que necesita
        el modelo: `id,nombre,descripcion,fecha de expiracion....`
    """

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
    account_id       = db.Column(db.Integer,db.ForeignKey("accounts.id",ondelete="CASCADE"))
    expiration_date  = db.Column(db.Date(),nullable=False)
    #relaciones
    service_payments = db.relationship("Service_payment",back_populates="service")
    user             = db.relationship("User",back_populates="services")
    account          = db.relationship("Account",back_populates="accounts_serv")
    
    #Funciones para obtener datos del modelo servicio
    @staticmethod
    def get_all_by_userid(id:int):
        """
        Retorna todos los objetos del modelo Service en una lista, relacionados con el `usuario activo actualmente `\n
        :Ejemplo:
        ```
            return [service_object_1,service_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        all_services =db.session.execute(db.select(Service)).scalars()
        all_services_list =[]

        for service in all_services:
            if service.user_id == id:
                all_services_list.append(service)
        return all_services_list
    
    @staticmethod
    def get_all_for_payment(id:int):
        """
        Retorna todos los servicios disponibles para pagar relacionados con el `usuario activo actualmente`. \n
        :Ejemplo:
        ```
            return [service_object_1,service_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        all_services =db.session.execute(db.select(Service)).scalars()
        all_services_list =[]
        for service in all_services:
            if service.user_id == id and service.reamining_price>0:
                all_services_list.append(service)
        return all_services_list
    
    @staticmethod
    def get_all_amount_payment(id:int):
        """
        Retorna el costo total de todos servicios relacionados con el `usuario activo actualmente`. \n
        :Ejemplo:
        ```
            return 345800
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """

        all_services =db.session.execute(db.select(Service)).scalars()
        all_services_list =[]

        for service in all_services:
            if service.user_id == id:
                all_services_list.append(service.price-service.reamining_price)
        return sum(all_services_list)

    @staticmethod
    def get_all_by_category(category:str):
        all_services = db.session.execute(db.select(Service)).scalars()
        all_services_list=[]

        for service in all_services:
            if service.category==category:
                all_services_list.append(service)
        return all_services_list
    
    @staticmethod
    def get_full_amount(id:int):
        all_service = db.session.execute(db.select(Service)).scalars()
        amount = 0
        for service in all_service:
            if service.user_id == id:
                amount += service.price
        return amount
    
    @staticmethod
    def get_by_id(id):
        """
        Retorna el objeto del modelo `servicio` que coincida con el `id` proporcionado. \n
        :Ejemplo:
        ```
            return service_object_12
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """
        service = Service.query.filter_by(id=id).first()
        return service
    
    @staticmethod 
    def get_all_for_account(id:int,account_list:list):
        all_services =db.session.execute(db.select(Service)).scalars()
        all_services_list =[]
        all_acounts = [[] for account in account_list]
        x = 0
        for service in all_services:
            if service.user_id == id:
                all_services_list.append(service)
        for service in all_services_list:
            if service.account_id==(account_list[x]).id:
                all_acounts[x].append(service)
            x+=1
        return all_acounts
