from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,DateField,TextAreaField
from wtforms.validators import DataRequired,Length

class FormularioCrearPagoServicio(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",validators=[Length(0,200)])
    submit      = SubmitField("Ingresar pago de servicio")


class FormularioActualizarPagoServicio(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",Length(0,200))
    submit      = SubmitField("Actualizar pago de servicio")
    