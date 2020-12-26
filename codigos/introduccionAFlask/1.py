#codigo 1, ejemplo de como crear el objeto app, de como usar el decorador app.route y de como activar el modo debug desde el metodo run dentro del codigo
from flask import Flask#importamos desde flask la clase Flask, el modulo Flask previamente se instalo con el comando de terminal "pip3 install Flask"

app = Flask(__name__)#se instancia el objeto app de la clase Flask

@app.route("/")#se usa el decorador app.route que nos permitira llamar a la ruta dentro del parentesis desde el explorador y ejecutar la siguiente funcion
def index():
    return "Piensa libre"

if __name__ == "__main__":
    app.run(debug=True)#ejecutamos el metodo run de nuestro objeto app, que por defecto estara escuchando en el puerto 5000 de nuestro localhost, la opcion debug=True activa el modo debug
