from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioCrearIngreso(FlaskForm):
    nombre = StringField("Nombre",validators=[DataRequired(),Length(0,50)])
    fecha  = DateTimeField("Fecha",validators=[DataRequired()])
    monto  = IntegerField("Monto") 
    submit = SubmitField('Crear ingreso')

class FormularioActualizarIngreso(FlaskForm):
    nombre = StringField("Nombre",validators=[DataRequired(),Length(0,50)])
    fecha  = DateTimeField("Fecha",validators=[DataRequired()])
    monto  = IntegerField("Monto") 
    submit = SubmitField('Actualizar ingreso')