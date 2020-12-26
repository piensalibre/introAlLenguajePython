#codigo 7, ejemplo de creacion de url
from flask import Flask,request,url_for#se importa url_for para la creacion de url
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola"

@app.route("/piensa",methods = ["POST"])
def piensa():
    print(url_for("post", postId = 2))#url_for recibe como argumento el nombre de la funcion a la cual pertenece la url,esto imprime en terminal la direccion "/", si esta funcion recibe argumentos estos se pasa tambien, despues de una ',' y con su respectivo nombre y valor
    return "piensa"

@app.route("/post/<postId>",methods = ["POST"])
def post(postId):
    return "El id del post es: " + postId