from app import db 
from datetime import datetime
import calendar
class Loan_payment(db.Model):
    """
        Objeto que representa el modelo `Pago de prestamo`.

        Tiene las columnas con todos 
        datos necesarios que necesita
        el modelo: `id,monto,fecha,prestamo_id....`
    """

    __tablename__ = "loan_payments"

    #columnas
    id          = db.Column(db.Integer,primary_key=True)
    amount      = db.Column(db.Integer,nullable=False)
    date        = db.Column(db.DateTime(),nullable=False)
    description = db.Column(db.Text(),nullable=True)
    loan_id     = db.Column(db.Integer,db.ForeignKey("loans.id",ondelete="CASCADE"))
    user_id     = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    #relaciones
    user        = db.relationship("User",back_populates="loans_pay")
    loan        = db.relationship("Loan",back_populates="loan_payments")
    
    #Funciones para obtener datos del model 'pago de prestamos'
    @staticmethod 
    def get_all_by_userid(id:int):
        """
        Retorna todos los objetos del modelo Loan_payment en una lista, relacionados con el `usuario activo actualmente `\n
        :Ejemplo:
        ```
            return [loan_payment_object_1,loan_payment_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        all_loanpayments = db.session.execute(db.select(Loan_payment)).scalars()
        all_loanpayments_list =[]
        for payment in all_loanpayments:
            if payment.user_id== id:
                all_loanpayments_list.append(payment)
        return all_loanpayments_list
    
    @staticmethod 
    def get_all_by_userid_forsummary(id:int):
        """
        Retorna todos los objetos del modelo Loan_payment en una lista, relacionados con el `usuario activo actualmente` para el resumen.\n
        :Ejemplo:
        ```
            return [loan_payment_object_1,loan_payment_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        date_now = datetime.now()
        last_day = calendar.monthrange(date_now.year,date_now.month)                        
        end_date = datetime(date_now.year,date_now.month,last_day[1])
        start_date = datetime(date_now.year,date_now.month,1)

        all_loanpayments = db.session.execute(db.select(Loan_payment)).scalars()
        all_loanpayments_list =[]
        for payment in all_loanpayments:
            if payment.user_id== id and payment.date>start_date and payment.date<=end_date:
                all_loanpayments_list.append(payment)
        return all_loanpayments_list

    @staticmethod
    def get_all_amount_for_account(id:int,loans_accounts:list):
        """
        Retorna todos los pagos conservando la estructura de la `matriz loans_accounst` 
        que esta dividida en cuentas que contiene todos los prestamos.
        Lo hacemos es remplazar los `prestamos` por
        sus `pagos` de modo que cada cuenta va a tener los pagos de dichos prestamos.
        :Ejemplo:
        
        ```
        #antes
            return [
                [loan_object_1,loan_object_5],
                [loan_object_2,loan_object_12],
                [loan_object_4]
            ]
        ```
        ```
        #despues
            return [
                [4000,3000,2000,200],
                [50000,31000,3000],
                [32000]
            ]
            #Un prestamo puede tener mas de un pago

        ```
        :Parametros: id
        :id: = identificador unico de usuario.
        :loans_accounts: = matriz en la que cada fila representa una cuenta y dentro hay un prestamo relacionada con la misma.
        """


        date_now = datetime.now()
        last_day = calendar.monthrange(date_now.year,date_now.month)                        
        end_date = datetime(date_now.year,date_now.month,last_day[1])
        start_date = datetime(date_now.year,date_now.month,1)

        all_servicespayments = Loan_payment().get_all_by_userid(id)
        all_payments = [[] for account in loans_accounts]
        for payment in all_servicespayments:
            for row in loans_accounts:
                for loan in row:
                    if payment.loan_id == loan.id and payment.date>start_date and payment.date<end_date:
                        all_payments[loans_accounts.index(row)].append(payment.amount)
        return all_payments

    

