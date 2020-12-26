#codigo 10, ejemplo de uso de plantillas, la funcion render template buscara los templates dentro de la carpeta "templates", la cual debera estar incluida dentro de la carpeta raiz del proyecto
from flask import Flask,request,render_template#se importa la funcion render_template la cual retornara un template html
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola"

@app.route("/piensa",methods = ["GET","POST"])
def piensa():
    return render_template("piensa.html")#la funcion render_template toma como parametro una cadena con el nombre del template