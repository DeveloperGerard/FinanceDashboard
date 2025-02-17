from app import db 

class Account(db.Model):
    """
        Objeto que representa el modelo `Cuenta`.

        Tiene las columnas con todos 
        datos necesarios que necesita
        el modelo: `id,nombre,tarjeta....`
    """
     
    __tablename__ = "accounts"

    #columnas
    id            = db.Column(db.Integer,primary_key=True)
    account_name  = db.Column(db.String(50),nullable=False)
    card          = db.Column(db.String(50),nullable=False)
    user_id       = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    #relaciones
    user          = db.relationship("User",back_populates="accounts")
    accounts_loan = db.relationship("Loan",back_populates="account")
    accounts_serv = db.relationship("Service",back_populates="account")

    #Funciones para obtener datos del model 'pago de servicios'
    @staticmethod 
    def get_all_by_userid(id:int):
        """
        Retorna todos los objetos del modelo Account en una lista, relacionados con el `usuario activo actualmente `\n
        :Ejemplo:
        ```
            return [account_object_1,account_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """
         

        all_account = db.session.execute(db.select(Account)).scalars()
        all_account_list =[]
        for account in all_account:
            if account.user_id ==id:
                all_account_list.append(account)
        return all_account_list