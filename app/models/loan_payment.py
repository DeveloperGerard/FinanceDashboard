from app import db 

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
    def get_all_by_loanid(id:int):
        all_loanpayments = db.session.execute(db.select(Loan_payment)).scalars()
        all_loanpayments_list =[]
        for payment in all_loanpayments:
            if payment.loan_id == id:
                all_loanpayments_list.append(payment)
        return all_loanpayments_list
    
    @staticmethod 
    def get_all_by_userid(id:int):
        """
        Retorna todos los objetos del modelo Loan_payment en una lista, relacionados con el `usuario activo actualmente `
        ejemplo:
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
    def get_all_payment_for_loans(id:int,loans:list):
        all_loanpayments = db.session.execute(db.select(Loan_payment)).scalars()
        all_loanpayments_list =[]
        all_payments = [[] for loan in loans]
        x = 0
        for payment in all_loanpayments:
            for loan in loans:
                for subloan in loan:
                    if payment.loan_id == subloan.id:
                        all_payments[(loans).index(loan)].append(payment.amount)
        return all_payments

    

