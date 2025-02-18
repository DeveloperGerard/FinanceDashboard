from app import db


class Income(db.Model):
    __tablename__ = "incomes"

    #columnas
    id            = db.Column(db.Integer,primary_key=True)
    income_name   = db.Column(db.String(50),nullable=False)
    date          = db.Column(db.DateTime(),nullable=False)
    amount        = db.Column(db.Integer,nullable=False)
    user_id       = db.Column(db.Integer,db.ForeignKey("users.id",ondelete="CASCADE"))

    #relaciones
    user_id       = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    user          = db.relationship("User",back_populates="incomes")

    #Funciones para obtener datos del modelo ingreso
    @staticmethod
    def get_all_by_userid(id:int):
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
    