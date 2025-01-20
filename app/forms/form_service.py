from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,EmailField,IntegerField,SelectField,DateField,DateTimeField,TextAreaField
from wtforms.validators import DataRequired, Email,Length,EqualTo


class FormularioCrearServicio(FlaskForm):
    nombre          = StringField("Nombre",validators=[DataRequired(),Length(0,60)])
    description     = TextAreaField("Descripcion",validators=[Length(0,200)])
    date            = DateTimeField("Fecha")
    categoria       = StringField("Categoria:",validators=[DataRequired()])
    price           = IntegerField("Precio")
    submit          = SubmitField("Crear servicio")

class FormularioActualizarServicio(FlaskForm):
    nombre          = StringField("Nombre",validators=[DataRequired(),Length(0,60)])
    description     = TextAreaField("Descripcion",validators=[Length(0,200)])
    date            = DateTimeField("Fecha")
    categoria       = StringField("Categoria:",validators=[DataRequired()])
    price           = IntegerField("Precio")
    submit          = SubmitField("Actualizar servicio")
