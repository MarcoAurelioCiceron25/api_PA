#SQL Querys, el traductor de python a sql es SQLAlchemy

from extensions import db

#Importamos el modulo para hashear las contraseñas
from werkzeug.security import check_password_hash, generate_password_hash
# Generate_password_hash cambia un texto plano por un cript de caracteres con longitud igual en todos los casos
#check_password recibe dos datos:1) el hash esta en la db, 2) la contraseña del user

#Creamos un modelo para visualizar la tabla en sql
class Usuario(db.Model):
    __tablename__ = "Usuarios"
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    correo = db.Column(db.String(80), nullable=False)
    password = db.Column(db.String, nullable=False)

# Este el metódo para cifrar las contraseñas
    def hashear_password(self, password_original):
         self.password = generate_password_hash(password_original)

    
    def verificar_password(self):
        pass

   
    def save(self):
        #Creamos una conexión con la base de datos
        db.session.add(self)

#Nos aseguramos de que los cambios se hagan
        db.session.commit()

    def delete(self):
        db.session.delete(self)

        #nos aseguramos de que los cambios se guarde
        db.session.commit()


         