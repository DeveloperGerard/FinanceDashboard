from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,DateField
from wtforms.validators import DataRequired,Length,NumberRange

class FormularioCrearPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=4,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cuota',validators=[DataRequired(),NumberRange(1)])
    tea      = IntegerField('Tea',validators=[NumberRange(0)])
    fecha    = DateField("Fecha")
    fecha_vencimiento = DateField("Vencimiento")
    submit   = SubmitField('Crear prestamo')

class FormularioActualizarPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=0,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cuota',validators=[DataRequired()])
    tea      = IntegerField('Tea',validators=[DataRequired()])
    submit   = SubmitField('Actualizar prestamo')