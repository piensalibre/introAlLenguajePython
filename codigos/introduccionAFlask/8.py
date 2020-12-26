#codigo 8, ejemplo de redireccionamiento de usuario
from flask import Flask, request, url_for, redirect#se llama a redirect que se encargara de redireccionar al usuario
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola"

@app.route("/post/<postId>",methods = ["GET","POST"])
def post(postId):
    if request.method == "GET":
        return "El id del post es: " + postId
    else:
        return "Este no es el verbo GET"

@app.route("/piensa",methods = ["GET","POST"])
def piensa():
    return redirect(url_for("post",postId = 2))#la funcion redirect recibe como argumento la direccion, se retorna redirect para que se muestre al usuario