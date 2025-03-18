from flask import Flask, render_template, request, redirect, url_for

from methods import crear_cuenta, iniciar_sesion

def cargar_rutas(app):
    # Base de todas las rutas
    @app.route('/')
    def pagina():
        return render_template("index.html")

    @app.route('/login')
    def informacion():
        return render_template("login.html")

    @app.route('/signup')
    def datos():
        return render_template("signup.html")

    # Ruta que maneja la información del login
    @app.route('/manipulacion', methods=["POST"])
    def manipular_datos():
        correo = request.form.get('email')
        password = request.form.get('password')
        print(f'''
            Correo: {correo}
            Contraseña: {password}
        ''')

        iniciar_sesion()

        # Redirige a la página principal después de manejar los datos
        return redirect(url_for("pagina"))

    # Ruta para guardar información del usuario desde el signup
    @app.route('/datos_crear_cuenta', methods=["POST"])
    def obtener_datos_cuenta():
        nombre = request.form.get("name")
        correo = request.form.get("correo")
        password = request.form.get("password")
        print(f'''
            Nombre: {nombre}
            Correo: {correo}
            password: {password}
        ''')

        crear_cuenta(nombre, correo, password)
                                            

        # Redirige a la página principal después de registrar los datos
       
        return redirect(url_for("pagina"))
