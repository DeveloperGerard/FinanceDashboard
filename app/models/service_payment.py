from app import db 
from datetime import datetime
import calendar
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
    def get_all_by_userid_forsummary(id:int):
        """
        Retorna todos los objetos del modelo Service_payment en una lista, relacionados con el `usuario activo actualmente` para el resumen.\n
        :Ejemplo:
        ```
            return [service_payment_object_1,service_payment_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        date_now = datetime.now()
        last_day = calendar.monthrange(date_now.year,date_now.month)                        
        end_date = datetime(date_now.year,date_now.month,last_day[1])
        start_date = datetime(date_now.year,date_now.month,1)

        all_servicepayments = db.session.execute(db.select(Service_payment)).scalars()
        all_servicepayments_list =[]
        for payment in all_servicepayments:
            if payment.user_id== id and payment.date>start_date and payment.date<end_date:
                all_servicepayments_list.append(payment)
        return all_servicepayments_list

    @staticmethod
    def get_all_amount_for_account(id:int,services_accounts:list):
        """
        Retorna todos los pagos conservando la estructura de la `matriz services_accounts` 
        que esta dividida en cuentas que contiene todos los servicios.
        Lo hacemos es remplazar los `servicios` por
        sus `pagos` de modo que cada cuenta va a tener los pagos de dichos servicios.
        :Ejemplo:
        
        ```
        #antes
            return [
                [service_object_1,service_object_5],
                [service_object_2,service_object_12],
                [service_object_4]
            ]
        ```
        ```
        #despues
            return [
                [4000,3000,2000,200],
                [50000,31000,3000],
                [32000]
            ]
            #Un servicio puede tener mas de un pago

        ```
        :Parametros: id
        :id: = identificador unico de usuario.
        :services_accounts: = matriz en la que cada fila representa una cuenta y dentro hay un servicio relacionada con la misma.
        """


        date_now = datetime.now()
        last_day = calendar.monthrange(date_now.year,date_now.month)                        
        end_date = datetime(date_now.year,date_now.month,last_day[1])
        start_date = datetime(date_now.year,date_now.month,1)
        
        all_servicespayments = Service_payment().get_all_by_userid(id)
        all_payments = [[] for account in services_accounts]
        for payment in all_servicespayments:
            for row in services_accounts:
                for service in row:
                    if payment.service_id == service.id and payment.date>start_date and payment.date<end_date:
                        all_payments[services_accounts.index(row)].append(payment.amount)
        return all_payments




