from flask_wtf import FlaskForm
from  wtforms import StringField,SubmitField
#Formulario de registro de nuevo producto
class NewProductForm(flaskForm):
    nombre = StringField("Ingrese nombre:")
    precio = StringField("Ingrese precio:")
    submit = SubmitField("Registrar")