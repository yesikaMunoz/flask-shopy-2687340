#Dependencia de flask 
from flask import Flask
#Dependencia de los modelos 
from flask_sqlalchemy import SQLAlchemy
#Dependencia de la migracion 
from flask_migrate import Migrate
#Dependecia para echa y hora
from datetime import datetime 

#crear el objeto flask 
app = Flask(__name__)

#La 'cadena de conexion'(connectionstring)
app.config['SQLALCHEMY_DATABASE_URI'] ='mysql://root:@localhost/flask-shopy-2687340'
app.config['SQLALCHEMY_TRACK_NOTIFICATIONS']= False

#Crear el objeto de modelos 
db = SQLAlchemy(app) 
#Crear el objeto de la migracion 
migrate = Migrate(app,db)

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