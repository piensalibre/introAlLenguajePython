#codigo 13, ejemplo de uso de base de datos en flask
from flask import Flask,render_template
import mysql.connector
miBD = mysql.connector.connect(
    host = "localhost",
    username = "piensa",
    password = "piensa",
    database = "prueba"
)
cursor = miBD.cursor(dictionary=True)#dictionary True permite llamar a las columnas de la base de datos por su nombre y no por un numero de indice, ya que ahora no son tuplas sino diccionarios
app = Flask(__name__)
@app.route("/")
def index():
    cursor.execute("select * from Usuario")
    usuarios = cursor.fetchall()
    return render_template("usuarios.html",usuarios = usuarios)