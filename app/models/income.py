from app import db

class Income(db.Model):
    """
        Objeto que representa el modelo `Ingreso`.

        Tiene las columnas con todos 
        datos necesarios que necesita
        el modelo: `id,precio,nombre,fecha,monto....`
    """

    __tablename__ = "incomes"

    #columnas
    id             = db.Column(db.Integer,primary_key=True)
    income_name    = db.Column(db.String(50),nullable=False)
    income_date    = db.Column(db.DateTime(),nullable=False)
    description    = db.Column(db.String(150),nullable=False) 
    category       = db.Column(db.String(100),nullable=False)
    next_income    = db.Column(db.DateTime(),nullable=False)
    amount         = db.Column(db.Integer,nullable=False)
    user_id        = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))
    pending_amount = db.Column(db.Integer,nullable=False)

    #!FECHA PAGO-PENDIENTE-PROYECTADO-RECIBIIDO-CATEGORIA

    #relaciones
    user          = db.relationship("User",back_populates="incomes")

    #Funciones para obtener datos del modelo ingreso
    @staticmethod
    def get_all_by_userid(id:int):
        """
        Retorna todos los objetos del modelo Income en una lista, relacionados con el `usuario activo actualmente `\n
        :Ejemplo:
        ```
            return [income_object_1,income_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        all_incomes = db.session.execute(db.select(Income)).scalars()
        all_incomes_list =[]
        for income in all_incomes:
            if income.user_id ==id:
                all_incomes_list.append(income)
        return all_incomes_list
    
    @staticmethod 
    def get_full_amount():
        all_incomes = db.session.execute(db.select(Income)).scalars()
        amount = 0
        for income in all_incomes:
            amount+= income.price
        return amount
    
    @staticmethod 
    def get_full_reamining_amount():
        all_incomes = db.session.execute(db.select(Income)).scalars()
        amount = 0
        for income in all_incomes:
            amount += income.reamining_price
        return amount
    
    @staticmethod
    def get_all_by_category(id:int):
        """
        Retorna todos los objetos del modelo Income en una lista relacionados con el `usuario activo actualmente `
        ejemplo:
        ```
            return [income_object_1,income_object_2]
        ```
        :Parametros: id
        :id: = identificador unico de usuario
        """


        all_incomes = db.session.execute(db.select(Income)).scalars()
        all_incomes_list ={'Sueldo':[],'Horas extras':[],"Venta":[],"Inversiones":[]}
        for income in all_incomes:
            if income.user_id ==id:
                if income.category == 'Sueldo':
                    all_incomes_list['Sueldo'].append(income)
                elif income.category == 'Horas extras':
                    all_incomes_list['Horas extras'].append(income)
                elif income.category == 'Venta':
                    all_incomes_list['Venta'].append(income)
                else:
                    all_incomes_list['Inversiones'].append(income)
        return all_incomes_list
    