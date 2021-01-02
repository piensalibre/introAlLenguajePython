import os#os nos permite acceder a ciertas cosas del sistema operativo, como las variables de entorno

from flask import Flask

def create_app():#al separar todo en distintos modulos tenemos que crear esta funcion
    app = Flask(__name__)

    app.config.from_mapping(
        SECRET_KEY = "mIKeY",
        DATABASE_HOST = os.environ.get("FLASK_DATABASE_HOST"),#con "os.environ.get" sacamos de variables de entorno los valores que se asignaran a las variables dentro de flask
        DATABASE_PASSWORD = os.environ.get("FLASK_DATABASE_PASSWORD"),
        DATABASE_USER = os.environ.get("FLASK_DATABASE_USER"),
        DATABASE = os.environ.get("FLASK_DATABASE"),
    )

    from . import db#se manda a llamar el archivo db.py

    db.init_app(app)#se pasa app a la funcion init_app para cerrar la conexion a la base de datos

    from . import auth#se importa auth desde el directorio actual
    from . import todo#se manda a llamar el archivo todo.py

    app.register_blueprint(auth.bp)#se registra el blueprint que creamos en auth
    app.register_blueprint(todo.bp)#se registra el blueprint que creamos en auth

    @app.route("/hola")
    def hola():
        return "HOLA"
    
    return app