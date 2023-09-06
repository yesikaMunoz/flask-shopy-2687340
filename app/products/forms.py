from flask_wtf import FlaskForm
from  wtforms import StringField,SubmitField, IntegerField
from wtforms.validators import  InputRequired,NumberRange
from flask_wtf.file import FileField,FileRequired,FileAllowed
#Formulario de registro de nuevo producto
class NewProductForm(FlaskForm):
    nombre = StringField(validators=[InputRequired(message="Falta nombre")],
                    label="Ingrese nombre:")
    precio = IntegerField(label="Ingrese precio:",
                          validators=[
                              InputRequired(message="Falta precio"),
                              NumberRange(message="precio fuera de rango",
                                          min=1000,
                                          max=10000),
                              ])
    imagen = FileField(label="Cargue imagen del producto",
                       validators=[
                           FileRequired(message="Suba una imagen"),
                           FileAllowed(["jpg","png"],
                                       message="Debe seleccionar una imagen")
                       ])
    submit = SubmitField("Registrar")