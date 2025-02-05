from flask_wtf import FlaskForm
from wtforms import SubmitField,IntegerField,TextAreaField,DateTimeLocalField
from wtforms.validators import DataRequired,Length

class FormularioCrearPagoPrestamo(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateTimeLocalField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",validators=[Length(0,200)])
    submit      = SubmitField("Ingresar pago de prestamo")


class FormularioActualizarPagoPrestamo(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateTimeLocalField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",Length(0,200))
    submit      = SubmitField("Actualizar pago de prestamo")
    