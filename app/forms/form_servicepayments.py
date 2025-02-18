from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField,TextAreaField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioCrearPagoServicio(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",Length(0,200))
    submit      = SubmitField("Ingresar pago de servicio")


class FormularioActualizarPagoServicio(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",Length(0,200))
    submit      = SubmitField("Actualizar pago de servicio")
    