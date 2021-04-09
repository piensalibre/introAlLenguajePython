from flask import Flask,render_template,request
import formcff2

app = Flask(__name__)



@app.route("/",methods=["GET","POST"])
def index2 ():
    comment = formcff2.CommentForm(request.form)
    if request.method == "POST" and comment.validate():
        print (comment.username.data)
        print (comment.email.data)
        print (comment.comment.data)
    else:
        print("Error en el formulario")
    return render_template("cf3.html", Form=comment)

if __name__ == "__main__":
    app.run(debug=True,port=5000)