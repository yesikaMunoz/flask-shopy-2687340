#Dependencia de flask 
from flask import Flask
#depedencia de confiuracion
from .config import Config  
#Dependencia de los modelos 
from flask_sqlalchemy import SQLAlchemy
#Dependencia de la migracion 
from flask_migrate import Migrate

#crear el objeto flask 
app = Flask(__name__)
#configuracion del objeto flask
app.config.from_object(Config)


#Crear el objeto de modelos 
db = SQLAlchemy(app) 
#Crear el objeto de la migracion 
migrate = Migrate(app,db)

#importar los modelos de .models
from .models import Cliente,Producto,Venta,Detalle

