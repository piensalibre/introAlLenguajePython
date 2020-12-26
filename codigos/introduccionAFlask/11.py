#codigo 11, ejemplo de responder con json
from flask import Flask
app = Flask(__name__)
@app.route("/")
def index():
    return "Hola mundo"
@app.route("/piensa")
def piensa():
    return {
        "usuario":"piensa",
        "email":"micorreo"
    }#para responder con json solo debemos responder con un diccionario