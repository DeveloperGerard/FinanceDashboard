from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,DateField,RadioField
from wtforms.validators import DataRequired,Length

class FormularioCrearIngresoProgamado(FlaskForm):
    nombre          = StringField("Nombre",validators=[DataRequired(),Length(2,50)])
    descripcion     = StringField("Descripcion",validators=[DataRequired(),Length(0,150)])
    categoria       = RadioField("Categoria",validators=[DataRequired()],choices=['Sueldo','Horas extras','Venta','Inversiones'])
    monto           = IntegerField("Monto que esperas recibir")
    proximo_pago    = DateField("Proximo pago",validators=[DataRequired()])
    submit          = SubmitField('Crear ingreso')

class FormularioActualizarIngresoProgramado(FlaskForm):
    monto_recibido = IntegerField("Monto recibido",validators=[DataRequired()])
    proximo_pago    = DateField("Proximo pago",validators=[DataRequired()])
    submit          = SubmitField('Actualizar ingreso',validators=[DataRequired()])