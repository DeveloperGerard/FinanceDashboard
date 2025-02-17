from app import db 

class Service_payment(db.Model):
    """
        Objeto que representa el modelo `Pago de servicio`.

        Tiene las columnas con todos 
        datos necesarios que necesita
        el modelo: `id,fecha,descripcion,monto....`
    """

    __tablename__ = "service_payments"

    #columnas
    id          = db.Column(db.Integer,primary_key=True)
    amount      = db.Column(db.Integer,nullable=False)
    date        = db.Column(db.DateTime(),nullable=False)
    description = db.Column(db.Text(),nullable=True)
    service_id  = db.Column(db.Integer,db.ForeignKey("services.id",ondelete="CASCADE"))
    user_id     = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    #relaciones
    user        = db.relationship("User",back_populates="services_pay")
    service     = db.relationship("Service",back_populates="service_payments")

    #Funciones para obtener datos del model 'pago de servicios'
    @staticmethod 
    def get_all_by_serviceid(id:int):
        all_servicepayments = db.session.execute(db.select(Service_payment)).scalars()
        all_servicepayments_list =[]
        for payment in all_servicepayments:
            if payment.loan_id == id:
                all_servicepayments_list.append(payment)
        return all_servicepayments_list
    
    @staticmethod 
    def get_all_by_userid(id:int):
        """
        Retorna todos los objetos del modelo Service_payment en una lista, relacionados con el `usuario activo actualmente `\n
        :Ejemplo:
        ```
            return [service_payment_object_1,service_payment_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        all_servicepayments = db.session.execute(db.select(Service_payment)).scalars()
        all_servicepayments_list =[]
        for payment in all_servicepayments:
            if payment.user_id== id:
                all_servicepayments_list.append(payment)
        return all_servicepayments_list
    
    @staticmethod
    def get_all_payment_for_loans(id:int,services:list):
        all_servicepayments = db.session.execute(db.select(Service_payment)).scalars()
        all_servicepayments_list =[]
        all_payments = [[] for service in services]
        x = 0
        for payment in all_servicepayments:
            for service in services:
                for subservice in service:
                    if payment.service_id == subservice.id:
                        all_payments[(services).index(service)].append(payment.amount)
        return all_payments
