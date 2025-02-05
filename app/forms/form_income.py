from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,DateTimeLocalField
from wtforms.validators import DataRequired,Length

class FormularioCrearIngreso(FlaskForm):
    nombre = StringField("Nombre",validators=[DataRequired(),Length(0,50)])
    fecha  = DateTimeLocalField("Fecha",validators=[DataRequired()])
    monto  = IntegerField("Monto") 
    submit = SubmitField('Crear ingreso')

class FormularioActualizarIngreso(FlaskForm):
    nombre = StringField("Nombre",validators=[DataRequired(),Length(0,50)])
    fecha  = DateTimeLocalField("Fecha",validators=[DataRequired()])
    monto  = IntegerField("Monto") 
    submit = SubmitField('Actualizar ingreso')