from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,IntegerField,DateField
from wtforms.validators import DataRequired,Length,NumberRange

class FormularioCrearPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=4,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cuota',validators=[DataRequired(),NumberRange(1)])
    tea      = IntegerField('Tea',validators=[NumberRange(0)])
    fecha_vencimiento = DateField("Vencimiento")
    submit   = SubmitField('Crear prestamo')

class FormularioActualizarPrestamos(FlaskForm):
    nombre   = StringField('Nombre',validators=[DataRequired(),Length(min=0,max=50)])
    titular  = StringField('Titular',validators=[DataRequired(),Length(min=4,max=50)])
    precio   = IntegerField('Precio',validators=[DataRequired()])
    cuota    = IntegerField('Cuota',validators=[DataRequired()])
    tea      = IntegerField('Tea',validators=[DataRequired()])
    submit   = SubmitField('Actualizar prestamo')

#CON LOS QUE LO VOY A HACER form_scheduled_income y service_form
#HASTA HORA DOS OPCIONES
#?1 USAR LA FECHA COMO FECHA DE CREACION Y SACARLA DE FORMULARIO
#?ENTONCES LO QUE HARIA EL USUARIO ES IR ACTUALIZANDO LA FECHA DE VENCIMIENTO DESPUES DE CADA PAGO 
#?CLARO QUE DESPUES DE QUE EL MONTO DEL PRESTAMO SEA CUBRIDO NO SE PUEDE PAGAR
#?Y RECORDAR AL USUARIO DE ACTUALIZAR LAS FECHAS DE FENCIMIENTO

#!2 TENER UNA FECHA DE VENCIMIENTO Y LA OTRA PROXIMO VENCIMIENTO Y LO QUE PASARIA QUE EL USUARIO
#! AL HACER EL PAGO EN LA FECHA DE VENCIMIENTO ESTA RETROCEDERIA Y DEBERIA ACTUALIZAR CON OTRO FECHA_VENCIMIENTO--_PROXIMA
#  