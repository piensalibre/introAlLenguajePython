from flask import Flask,render_template,make_response,request,session
from flask.helpers import url_for
from flask_wtf import CSRFProtect
from werkzeug.utils import redirect
import formcff3

app = Flask(__name__)
app.secret_key = "dsfsdfsdfsdfsdfsdfsdfsd"
csrf =CSRFProtect(app)

@app.route("/",methods=["GET","POST"])
def index2 ():
    login = formcff3.LoginForm(request.form)
    if request.method == "POST" and login.validate():
        session["username"]=login.username.data
    return render_template("cf4.html", Form=login)

@app.route("/cookie")
def cookie ():
    response = make_response(render_template("cf5.html"))
    response.set_cookie("cookiePersonalizada","Piensa")
    return response

@app.route("/index")
def index():
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

if __name__ == "__main__":
    app.run(debug=True,port=5000)