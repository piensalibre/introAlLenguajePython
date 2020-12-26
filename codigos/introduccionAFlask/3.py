#codigo 3, ejemplo de como ingresar variables dentro de las rutas
from flask import Flask
app=Flask(__name__)

@app.route("/")
def index():
    return "Piensa libre"

@app.route("/post/<postId>")#se usan los signos "<>" para encerrar la variable que vamos a usar mas adelante en el codigo 
def postId(postId):#se pasa la variable que necesita el decorador
    return "El id del post es: " + postId
