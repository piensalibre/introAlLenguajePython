from flask import Flask,render_template,make_response,request,session,flash
from flask.helpers import url_for
from flask_wtf import CSRFProtect
from werkzeug.utils import redirect
import json
import formcff3
 
app = Flask(__name__)
app.secret_key = "dsfsdfsdfsdfsdfsdfsdfsd"
csrf =CSRFProtect(app)

@app.errorhandler(404)
def error404(e):
    return render_template("cf8.html"),404


@app.route("/",methods=["GET","POST"])
def index2 ():
    login = formcff3.LoginForm(request.form)
    if request.method == "POST" and login.validate():
        username=login.username.data
        succes="Bienvenido {}".format(username)
        flash(succes)
        flash(succes)
        flash(succes)
        session["username"]=login.username.data
    return render_template("cf7.html", Form=login)

@app.route("/cookie")
def cookie ():
    response = make_response(render_template("cf5.html"))
    response.set_cookie("cookiePersonalizada","Piensa")
    return response

@app.route("/index")
def index():
    print("index")
    if "username" in session:
        username = session["username"]
        print(username)
    cookiePersonalizada = request.cookies.get("cookiePersonalizada","indefinido")
    print(cookiePersonalizada)
    return render_template("cf6.html")

@app.route("/salir")
def salir():
    if "username" in session:
        session.pop("username")
    return redirect(url_for("index2"))

@app.route("/ajaxLogin",methods=["POST"])
def ajaxLogin():
    print(request.form)
    username = request.form['username']
    response = {'status':200, 'username':username, "id":1,"si":"jajaja"}
    print(response)
    return json.dumps(response)

    

if __name__ == "__main__":
    app.run(debug=True,port=5000)