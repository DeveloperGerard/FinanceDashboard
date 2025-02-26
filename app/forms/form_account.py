from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired,Length

class FormularioCrearCuenta(FlaskForm):
    nombre      = StringField('Nombre',validators=[DataRequired(),Length(2,50)])
    tarjeta     = StringField('Tarjeta',validators=[DataRequired(),Length(2,50)])
    submit      = SubmitField('Crear cuenta')
class FormularioActualizarCuenta(FlaskForm):
    nombre      = StringField('Nombre',validators=[Length(0,50)])
    tarjeta     = StringField('Tarjeta',validators=[DataRequired(),Length(0,50)])
    submit      = SubmitField('Actualizar cuenta')