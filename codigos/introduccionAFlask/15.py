#codigo 15, ejemplo de codigo en flask
from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/")
def index():
    return "Index"

@app.route("/contacto")
def contacto():
    return "<h1>Contacto</h1>"

@app.route("/hola/<nombre>")
def hola(nombre):
    return f"<h1>Hola {nombre}</h1>"

@app.route("/inicio")
def inicio():
    diccionario = {"nombre":"Piensa libre", "num":1,"lista":[1,2,3,4,5]}
    return render_template("inicio.html", dic = diccionario)

@app.route("/homepiensa")
def home():
    return render_template("homepiensa.html")

@app.route("/cont",methods=["GET","POST"])
def cont():
    nombre = request.form.get("nombre")
    return render_template("cont.html",nombre=nombre)