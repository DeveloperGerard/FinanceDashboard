from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField
from wtforms.validators import DataRequired, Email,Length,EqualTo,NumberRange

class FormularioCrearPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=0,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cuota',validators=[DataRequired(),NumberRange(1)])
    tea      = IntegerField('Tea',validators=[NumberRange(0)])
    fecha    = DateField("Fecha")
    fecha_vencimiento = DateField("Vencimiento")
    tea_mora = IntegerField('Tea mora',validators=[NumberRange(0)])
    submit   = SubmitField('Crear prestamo')

class FormularioActualizarPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=0,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cuota',validators=[DataRequired()])
    tea      = IntegerField('Tea',validators=[DataRequired()])
    tea_mora = IntegerField('Tea mora',validators=[DataRequired()])
    submit   = SubmitField('Actualizar prestamo')