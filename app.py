from flask import Flask

#supabase password = ruoOnbM665xWi2LA

#Desde el archivo routes importamos cargar rutas
from routes import cargar_rutas

from extensions import db

app = Flask(__name__)

#Configuramos la app para conectarse con una db
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres.uwnojecofktezvycmsyz:ruoOnbM665xWi2LA@aws-0-us-west-1.pooler.supabase.com:6543/postgres"


#2 Desactivamos el trackeo de modificaciones
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

#Cargamos las rutas creadas desde routes.py
cargar_rutas(app)

app.run(port=8080)


