from flask import Flask,render_template,make_response,request,session,flash,g
from flask.helpers import url_for
from flask_wtf import CSRFProtect
from werkzeug.utils import redirect
import json
import formcff4
from config import DevelopmentConfig
from models import db, User,Comment
from helper import date_format 
app = Flask(__name__)
app.config.from_object(DevelopmentConfig)
csrf =CSRFProtect()

@app.errorhandler(404)
def error404(e):
    return render_template("cf8.html"),404

@app.before_request
def beforeReq():
    if "username" not in session:
        print(request.endpoint)
        print("El usuario necesita login")
    print(request.endpoint)
    print("antes del request")
    g.test = "test"
    print("antes del request")
    print(g.test)
    if "username" not in session and request.endpoint in ["comment"]:
        return redirect(url_for("index2"))
    elif "username" in session and request.endpoint in ["index2","create"]:
        print(session["username"])
        print(session["userId"])
        return redirect(url_for("index"))

@app.after_request
def afterReq(response):
    print("despues del request")
    print(g.test)
    return response


@app.route("/",methods=["GET","POST"])
def index2 ():
    login = formcff4.LoginForm(request.form)
    if request.method == "POST" and login.validate():
        username=login.username.data
        password=login.password.data

        user = User.query.filter_by(username = username).first()
        if user is not None and user.verifyPassword(password):
            succes="Bienvenido {}".format(username)
            flash(succes)
            session["username"]=username
            session["userId"]=user.id
            return redirect(url_for("index"))
        else:
            errorMessage = "Usuario o contrasena no valida"
            flash(errorMessage)

        session["username"]=login.username.data
    return render_template("cf9.html", Form=login)

@app.route("/cookie")
def cookie ():
    response = make_response(render_template("cf5.html"))
    response.set_cookie("cookiePersonalizada","Piensa")
    return response

@app.route("/index")
def index():
    print("index desde el print")
    print(g.test)
    if "username" in session:
        username = session["username"]
        print(username)
    # cookiePersonalizada = request.cookies.get("cookiePersonalizada","indefinido")
    # print(cookiePersonalizada)
    return render_template("cf6.html")

@app.route("/salir")
def salir():
    if "username" in session:
        session.pop("username")
        session.pop("userId")
    return redirect(url_for("index2"))

@app.route("/ajaxLogin",methods=["POST"])
def ajaxLogin():
    print(request.form)
    username = request.form['username']
    response = {'status':200, 'username':username, "id":1,"si":"jajaja"}
    print(response)
    return json.dumps(response)

@app.route("/create",methods = ["GET","POST"])
def create():
    createForm =formcff4.CreateForm(request.form)
    if request.method == 'POST' and createForm.validate():
        user = User(createForm.username.data,
        createForm.password.data,
        createForm.email.data)
        db.session.add(user)
        db.session.commit()
        succesMessage = "Usuario registrado"
        flash(succesMessage)
    return render_template("cf10.html",Form=createForm)


@app.route("/reviews",methods=["GET"])
@app.route("/reviews/<int:pagina>",methods=["GET"])
def reviews(pagina=1):
    porPagina = 3
    commentList=Comment.query.join(User).add_columns(User.username, Comment.text,Comment.created_date).paginate(pagina,porPagina,False)

    return render_template("cf12.html",commentList=commentList,date_format= date_format)

@app.route("/comment",methods=["GET","POST"])
def comment():
    comment = formcff4.CommentForm(request.form)
    if request.method == "POST" and comment.validate():
        userId = session["userId"]
        commento = Comment(userId = userId ,text=comment.comment.data)
        db.session.add(commento)
        db.session.commit()
        succes = "nuevo comentario creado"
        flash(succes)

    return render_template("cf11.html", Form=comment)
    

if __name__ == "__main__":
    csrf.init_app(app)
    db.init_app(app)
    with app.app_context():
        db.create_all()
    app.run()