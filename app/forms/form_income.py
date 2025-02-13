from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField,RadioField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioCrearIngreso(FlaskForm):
    nombre          = StringField("Nombre",validators=[DataRequired(),Length(0,50)])
    fecha_pago      = DateField("Fecha de pago",validators=[DataRequired()])
    descripcion     = StringField("Descripcion",validators=[DataRequired(),Length(0,150)])
    categoria       = RadioField("Categoria:",validators=[DataRequired()],choices=['Sueldo','Horas extras','Venta','Inversiones'])
    monto           = IntegerField("Monto")
    proximo_pago    = DateField("Proximo pago:",validators=[DataRequired()])
    monto_pendiente = IntegerField("Monto pendiente")
    submit          = SubmitField('Crear ingreso')

class FormularioActualizarIngreso(FlaskForm):
    nombre = StringField("Nombre",validators=[DataRequired(),Length(0,50)])
    fecha  = DateField("Fecha",validators=[DataRequired()])
    monto  = IntegerField("Monto") 
    submit = SubmitField('Actualizar ingreso')