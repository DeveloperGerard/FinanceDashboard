from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField
from wtforms.validators import DataRequired,Length

class FormularioCrearCuenta(FlaskForm):
    nombre      = StringField('Nombre de la Cuenta',validators=[DataRequired(),Length(2,50)],
                              render_kw={"placeholder": "Ej: Cuenta Corriente"})
    tarjeta     = StringField('Número Cuenta/Tarjeta',validators=[DataRequired(),Length(2,50)],
                              render_kw={"placeholder": "Ej: 1234 5678 9012 3456 / Recomendamos usar sólo los últimos 4 dígitos"})
    saldo       = IntegerField('Saldo Actual',validators=[DataRequired()],
                               render_kw={"placeholder": "Ej: 1000"})
    submit      = SubmitField('Crear cuenta')
class FormularioActualizarCuenta(FlaskForm):
    nombre      = StringField('Nombre de la Cuenta',validators=[Length(2,50)],
                              render_kw={"placeholder": "Ej: Cuenta Corriente"})
    tarjeta     = StringField('Número Cuenta/Tarjeta',validators=[DataRequired(),Length(2,50)],
                              render_kw={"placeholder": "Ej: 1234 5678 9012 3456 / Recomendamos usar sólo los últimos 4 dígitos"})
    submit      = SubmitField('Actualizar cuenta')