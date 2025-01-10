from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioRegistro(FlaskForm):
    nombre               = StringField('Nombre',validators=[DataRequired(),Length(min=3,max=64)])
    email                = EmailField('Gmail',validators=[DataRequired(),Email()])
    contraseña           = PasswordField('Contraseña',validators=[DataRequired(),Length(min=8,max=128),EqualTo('confirmar_contraseña',message="Las contraseñas deben ser iguales")])
    confirmar_contraseña = PasswordField('Confirmar contraseña',validators=[DataRequired()])
    submit               = SubmitField('Registrarse')

class FormularioInicio(FlaskForm):
    email      = EmailField('Gmail',validators=[DataRequired(),Email()])
    contraseña = PasswordField('Contraseña',validators=[DataRequired(),Length(min=8,max=128)])
    submit     = SubmitField("Iniciar sesion")