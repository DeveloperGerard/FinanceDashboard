from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField,TextAreaField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioCrearPagoPrestamo(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",validators=[Length(0,200)])
    submit      = SubmitField("Ingresar pago de prestamo")


class FormularioActualizarPagoPrestamo(FlaskForm):
    monto       = IntegerField("Monto",validators=[DataRequired()])
    fecha       = DateField("Fecha",validators=[DataRequired()])
    descripcion = TextAreaField("Descripcion",Length(0,200))
    submit      = SubmitField("Actualizar pago de prestamo")
    