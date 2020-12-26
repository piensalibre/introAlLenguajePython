#codigo 14
from flask import Flask,render_template,request,url_for,redirect
from flask.helpers import url_for
import mysql.connector

app = Flask(__name__)

miDB = mysql.connector.connect(
    host = "localhost",
    username = "piensa",
    password = "piensa",
    database = "prueba"
)

cursor = miDB.cursor(dictionary=True)

@app.route("/piensa",methods = ["POST","GET"])
def piensa():
    cursor.execute("select * from Usuario")
    usuarios = cursor.fetchall()
    return render_template("usuarios.html",usuarios = usuarios)

@app.route("/crear",methods = ["GET","POST"])
def crear():
    if request.method == "POST":
        username = request.form["username"]
        email = request.form["email"]
        edad = request.form["edad"]
        sql = "insert into Usuario(username,email,edad) values(%s,%s,%s)"
        values = (username,email,edad)
        cursor.execute(sql,values)
        miDB.commit()
        return redirect(url_for("piensa"))
    return render_template("crear.html")