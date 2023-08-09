#Dependencia de flask 
from flask import Flask, render_template
#Dependencia de los modelos 
from flask_sqlalchemy import SQLAlchemy
#Dependencia de la migracion 
from flask_migrate import Migrate
#Dependecia para echa y hora
from datetime import datetime 
#Dependencias de wtforms 
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField


#crear el objeto flask 
app = Flask(__name__)

#La 'cadena de conexion'(connectionstring)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False
app.config['SECRET_KEY']= 'ficha_2687340'
#Crear el objeto de modelos 
db = SQLAlchemy(app) 
#Crear el objeto de la migracion 
migrate = Migrate(app,db)

#Crer formulario de registro de productos
class ProductosFrom(FlaskForm):
     nombre = StringField(' ingresa nombre producto')
     precio = StringField('ingresa precio producto')
     submit = SubmitField('Regitrar Producto')
 
#crear los modelos cliente 
class Cliente(db.Model):
    #definir los atributos
    __tablename__="clientes"
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(120),
                         nullable=True)
    pasword = db.Column(db.String(128),
                        nullable=True)
    email= db.Column(db.String(100),
                        nullable=True)
#Relaciones de SQL alquemy 
    ventas = db.relationship('Venta', backref ="cliente", lazy="dynamic" )
#crear los modelos producto
class Producto(db.Model):
    #definir los atributos
    __tablename__="productos"
    id = db.Column(db.Integer, primary_key = True)
    nombre = db.Column(db.String(120))
    precio = db.Column(db.Numeric(precision = 10, scale =2))
    imagen = db.Column(db.String(200))
#crear los modelos 
class Venta (db.Model):
    #Definir los atributos
     __tablename__="ventas"
     id = db.Column(db.Integer, primary_key = True)
     fecha = db.Column(db.DateTime , default = datetime.utcnow)
     #clave foranea
     cliente_id = db.Column(db.Integer, db.ForeignKey('clientes.id'))
    #crear los modelos de dellate 
class Detalle (db.Model):
     #Definir los atributos
     __tablename__="detalles"
     id = db.Column(db.Integer, primary_key = True)
      #clave foranea
     producto_id = db.Column(db.Integer, db.ForeignKey('productos.id'))
       #clave foranea
     venta_id = db.Column(db.Integer, db.ForeignKey('ventas.id'))
     cantidad = db.Column(db.Numeric(precision = 10, scale =2))
     
     # Rutas :
@app.route('/productos', methods =['GET','POST'])
def nuevo_producto():
    form = ProductosFrom()
    if form .validate_on_submit():
    #Creamos un nuevo produto
        p = Producto(nombre= form.nombre.data,
                     precio = form.precio.data)
        db.session.add(p)
        db.session.commit()
        return "Producto registrado"
    return render_template('nuevo_produto.html',form =form)