#codigo 4, ejemplo de como cambiar el tipo de la variable mandada a la ruta
from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

@app.route("/post/<int:postId>")#con "int:" se hace que la variable sea de tipo entero
def postId(postId):
    return "El id del post es: {}".format(postId)#se hace uso del metodo format para devolver el entero dentro de la cadena, donde la variable se inserta en los corchetes
