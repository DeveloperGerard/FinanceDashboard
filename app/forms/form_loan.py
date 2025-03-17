from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,DateField,FloatField
from wtforms.validators import DataRequired,Length,NumberRange,InputRequired

class FormularioCrearPrestamos(FlaskForm):
    nombre      = StringField('Nombre',validators=[DataRequired(),Length(min=4,max=50)])
    titular     = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    descripcion = StringField("Descripcion",validators=[Length(0,160)])
    precio      = IntegerField('Precio',validators=[DataRequired()])
    cuota       = IntegerField('Cantidad de Cuotas',validators=[DataRequired(),NumberRange(1)])
    tea         = FloatField('Tea',validators=[NumberRange(min=0,max=100),InputRequired()],default=0)
    fecha_vencimiento = DateField("Vencimiento",validators=[DataRequired()])
    submit      = SubmitField('Crear prestamo')

class FormularioActualizarPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=0,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cantidad de Cuotas',validators=[DataRequired()])
    tea      = FloatField('Tea',validators=[NumberRange(min=0,max=100)])
    fecha_vencimiento = DateField("Vencimiento",validators=[DataRequired()])
    submit   = SubmitField('Actualizar prestamo')
