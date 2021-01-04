#codigo 16
from flask import Flask, render_template, request, redirect, url_for

tareas =[]

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("indextareas.html",tareas=tareas)

@app.route("/agregar",methods=["GET","POST"])
def agregar():
    if request.method == "GET":
        return render_template("agregartareas.html")
    else:
        tarea =request.form.get("tarea")
        tareas.append(tarea)
        return redirect(url_for("index"))