from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField
from wtforms.validators import DataRequired, Email,Length,EqualTo

class FormularioRegistro(FlaskForm):
    nombre               = StringField('Nombre',validators=[DataRequired(),Length(min=3,max=64)])
    email                = EmailField('Gmail',validators=[DataRequired(),Email(),Length(min=3,max=320)])
    clave                = PasswordField('clave',validators=[DataRequired(),Length(min=8,max=128),EqualTo('confirmar_clave',message="Las claves deben ser iguales")])
    confirmar_clave      = PasswordField('Confirmar clave',validators=[DataRequired()])
    submit               = SubmitField('Registrarse')

class FormularioInicio(FlaskForm):
    email      = EmailField('Gmail',validators=[DataRequired(),Email()])
    clave      = PasswordField('clave',validators=[DataRequired(),Length(min=8,max=128)])
    submit     = SubmitField("Iniciar sesion")

class FormularioCambiarContraseña(FlaskForm):
    clave     = PasswordField('clave',validators=[DataRequired(),Length(min=8,max=128),EqualTo('confirmar',message="Las claves deben ser iguales")])
    confirmar = PasswordField('Confirmar clave',validators=[DataRequired()])
    submit    = SubmitField('Cambiar contraseña')

class FormularioCambiarGmail(FlaskForm):
    email     = EmailField('Email',validators=[DataRequired(),Email(),Length(min=3,max=320),EqualTo('confirmar',message="Los correos deben ser iguales")])
    confirmar = EmailField('Repetir email',validators=[DataRequired(),Email(),Length(min=3,max=320)])
    submit    = SubmitField('Cambiar correo')