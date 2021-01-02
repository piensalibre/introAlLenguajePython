import mysql.connector
import click#nos permite ejecutar funciones desde terminal
from flask import current_app,g#current_app mantiene la aplicacion que estamos ejecutando, g es una variable que se encuentra en toda nuestra aplicacion, y se le puede ir asignando distintas variables para asi despues poder acceder a ellas desde otras partes de nuestra aplicacion
from flask.cli import with_appcontext#esto nos va a permitir usar el script de creacion de base de datos el contexto de nuestra aplicacion, como las variables de configuracion
from .schema import instructions#.schema contendra todas las intrucciones para la creacion de nuestra base de datos

def get_db():#esta funcion nos permitira obtener nuestra base de datos y el cursor dentro de nuestra aplicacion
    if 'db' not in g:#si db no se encuentra en g se ejecuta lo siguiente
        g.db = mysql.connector.connect(
            host = current_app.config['DATABASE_HOST'],#estamos configurando nuestra conexion en base a la configuracion de nuestra app
            user = current_app.config['DATABASE_USER'],
            password = current_app.config['DATABASE_PASSWORD'],
            database = current_app.config['DATABASE']
        )
        g.c = g.db.cursor(dictionary=True) 
    return g.db,g.c#retornamos la conexion y el cursor, de esta manera al llamar a getdb podemos interactuar con nuestra base de datos

def close_db(e = None):#esta funcion permite cerrar la conexion despues de hacer
    db = g.pop('db',None)#si existe la conexion db toma el valor de db, sino es None
    if db is not None:#si db tiene un valor distinto de None se procede a cerrar la conexion
        db.close()

def init_db():
    db,c = get_db()#se pasan los valores que retorna la funcion get_db a db y c, en este case db recibe los valores de la conexion y c al cursor
    for i in instructions:#debido a que todas las instrucciones para la creacion de la base de datos se encuentran dentro de una lista porque la libreria mysql.connector solo ejecuta una instruccion por vez y no un script, se debe iterar en el orden que se quiere que se ejecuten las lineas
        c.execute(i)
    db.commit()

@click.command('init-db')#se decora la funcion init_db_comand para que se pueda ejecutar desde la terminal, se pasa como argumento el nombre de como se mandara a llamar desde la terminal con el comando flask "nombre de la funcion"
@with_appcontext#se decora con with_appcontext para que pueda acceder al contexto de la aplicacion, como son las variables de conexion
def init_db_comand():
        init_db()#esta funcion ejecuta la logica para la creacion de la base de datos
        click.echo('Base de datos inicializada')#nos indica que la base de datos se inicializo de manera correcta

def init_app(app):#esta funcion se ejecutara al terminar la peticion, cuando elimine al contexto de la aplicacion
    app.teardown_appcontext(close_db)
    app.cli.add_command(init_db_comand)