#codigo 6,ejemplo de como mandar a consola datos de formulario
from flask import Flask,request
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/piensa",methods=["POST"])
def piensa():
    print(request.form)#esta linea imprime todos los datos enviados desde el formulario
    print(request.form["llave1"])#esta linea imprime los datos enviados a la llave dentro de los corchetes
    print(request.form["llave2"])
    return "piensa"