#codigo 2, este codigo no ejecuta el metodo run ya que este se ejecutara desde terminal, esto se hara indicandole a Flask donde se encuentra el ejecutable mediante el comando de terminal "export FLASK_APP=2.py, el modo debug se ejecutara cambiando el entorno de trabajo a modo desarrollo con el comando de terminal "export FLASK_ENV=development", una vez hecho esto podemos ejecutar el comando de terminal "flask run"
from flask import Flask
app = Flask(__name__)

@app.route("/")
def index():
    return "Hola mundo"

