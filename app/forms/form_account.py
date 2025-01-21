from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioCrearCuenta(FlaskForm):
    nombre      = StringField('Nombre',validators=[DataRequired(),Length(0,50)])
    tarjeta     = StringField('Tipo',validators=[DataRequired(),Length(0,50)])
    submit      = SubmitField('Crear cuenta')
class FormularioActualizarCuenta(FlaskForm):
    nombre      = StringField('Nombre',validators=[DataRequired(),Length(0,50)])
    tarjeta     = StringField('Tipo',validators=[DataRequired(),Length(0,50)])
    submit      = SubmitField('Actualizar cuenta')