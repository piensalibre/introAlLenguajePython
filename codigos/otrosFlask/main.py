from flask import Flask,request, make_response, redirect, render_template,session,url_for, flash
from flask_wtf import FlaskForm
from wtforms.fields import StringField, PasswordField,SubmitField
from wtforms.validators import DataRequired
import unittest
app = Flask(__name__)

app.config["SECRET_KEY"]="SUPER SECRETO"

todos = ["Todo1","Todo2","Todo3","Todo4"]

class LoginForm(FlaskForm):
    username = StringField("Nombre de usuario", validators=[DataRequired()])
    password = PasswordField("Password",validators=[DataRequired()])
    submit=SubmitField("Enviar")

@app.cli.command()
def test():
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner().run(tests)

@app.errorhandler(404)
def not_found(error):
    return render_template('404.html',error=error)

@app.route("/")
def index():
    userIp = request.remote_addr
    response = make_response(redirect("/hello"))
    # response.set_cookie("userIp",userIp)
    session["userIp"] = userIp
    print("Desde index "+str(session))
    return response

@app.route("/hello",methods=['GET','POST'])
def hello():
    # userIp = request.cookies.get("userIp")
    userIp = session.get("userIp")
    loginForm=LoginForm()
    username =session.get("username")
    context = {
        "userIp":userIp,
        "todos": todos,
        "loginForm":loginForm,
        "username":username 
    }
    if request.method == 'POST':#validateonsubmitconcsrf
        username = loginForm.username.data
        session['username'] = username
        flash("Nombre de usuario registrado con exito")
        print("Desde el post "+str(session))
        return redirect(url_for('index'))
    return render_template("hello.html",**context)
    