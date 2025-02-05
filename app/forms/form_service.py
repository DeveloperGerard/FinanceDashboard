from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,TextAreaField,RadioField,DateTimeLocalField
from wtforms.validators import DataRequired,Length


class FormularioCrearServicio(FlaskForm):
    nombre          = StringField("Nombre",validators=[DataRequired(),Length(0,60)])
    descripcion     = TextAreaField("Descripcion",validators=[Length(0,200)])
    fecha           = DateTimeLocalField("Fecha")
    categoria       = RadioField("Categoria:",validators=[DataRequired()],choices=['Entretencion','Telefonia','Informatica','Higiene','Alquiler','Academico','Transporte','Medico'])
    precio          = IntegerField("Precio")
    submit          = SubmitField("Crear servicio")

class FormularioActualizarServicio(FlaskForm):
    nombre          = StringField("Nombre",validators=[DataRequired(),Length(0,60)])
    descripcion     = TextAreaField("Descripcion",validators=[Length(0,200)])
    fecha           = DateTimeLocalField("Fecha")
    categoria       = StringField("Categoria:",validators=[DataRequired()])
    precio          = IntegerField("Precio")
    submit          = SubmitField("Actualizar servicio")
