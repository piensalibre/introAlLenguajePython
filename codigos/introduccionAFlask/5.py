#codigo 5, ejemplo de uso de verbos http
from flask import Flask,request#se importa tambien el metodo request para ser utilizado para diferenciar metodos si ambos son usados en la misma funcion decorada dentro de la misma ruta
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola"

@app.route("/post/<postId>",methods = ["GET","POST"])#se pasa como argumento la lista methods para decir que metodos son los que se van a utilizar, se pueden pasar varios metodos a la vez a la misma ruta o indicar uno por uno con una funcion diferente para la misma ruta segun el metodo
def postId(postId):
    if request.method == "GET":#en caso de usar los dos metodos en el mismo decorador se puede hacer uso del metodo request
        return "El numero del post es: " + postId
    else:
        return "Este no es el metodo GET"
