#Esto es para evitar las importaciones circulares

from flask_sqlalchemy import SQLAlchemy

#Creamos un objeto SQLAlchemy para controlar toda la base de datos
db = SQLAlchemy()