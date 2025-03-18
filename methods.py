from models import Usuario

#Un archivo que contiene todas las acciones de los usuarios
#Usamos method para que el user pueda crear una cuenta

def crear_cuenta(nombre, correo, password):
    #Creamos un objeto de tipo usuario que contenga la info para la db

    usuario_existente = Usuario.query.filter_by(correo=correo).first()

    if usuario_existente is not None:
        print("El correo ya existe en la db")
        return {"status": "error", "error": "La cuenta ya está registrada"}
    


    nuevo_usuario = Usuario(name=nombre, correo=correo)

    nuevo_usuario.hashear_password(password_original=password)

    nuevo_usuario.save()

    return {"status": "ok", "email":correo}

def iniciar_sesion():
    #contiene usuarios filtrados a traves de un parámetro
    usuarios_existentes = Usuario.query.filter_by(email="jose@correo.com")
    print(usuarios_existentes)