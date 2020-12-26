#codigo 12, ejemplo de como mandar variables a las plantillas y de como crear plantillas base que sirvan como plantillas padres para otras plantillas hijas que heredaran codigo de ellas
from flask import Flask,render_template,request
app = Flask(__name__)
@app.route("/",methods = ["GET"])
def index():
    return render_template("home.html", mensaje = "Hola mundo")