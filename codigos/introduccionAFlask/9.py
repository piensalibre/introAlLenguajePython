#codigo 9, ejemplo de como abortar la ejecucion de nuestro codigo
from flask import Flask,request,abort#se llama la funcion abort la cual detendra nuestro codigo
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola"

@app.route("/post/<postId>",methods = ["GET","POST"])
def post(postId):
    if request.method == "GET":
        return "El id del post es: " + postId
    else:
        return "Es otro verbo diferente a GET"

@app.route("/piensa",methods = ["GET","POST"])
def piensa():
    abort(401)#se le envia al usuario un codigo 401