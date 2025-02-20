from app import db

class Email_message(db.Model):
    """
    ⚠️El `usuario` no interectua con este modelo.⚠️\n
    Objeto que representa los mensajes que se envian diariamente por `email`.\n
    Contiene las columnas titulo,descripcion.
    
    """

    __tablename__   = "email_messages"


    id          = db.Column(db.Integer,primary_key=True)
    title       = db.Column(db.String(50),nullable=False)
    description = db.Column(db.Text,nullable=False)
    
    @staticmethod
    def get_all():
        """
        Retorna todos los objetos del modelo `mensajes de email` en una lista.\n
        :Ejemplo:
        ```
            return [email_message_1,email_message_2]
        ```
        """

        all_messages = db.session.execute(db.select(Email_message)).scalars()
        all_messages_list =[]
        for message in all_messages:
                all_messages_list.append(message)
        return all_messages_list