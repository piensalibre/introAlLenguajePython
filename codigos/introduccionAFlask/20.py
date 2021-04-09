from flask import Flask,render_template,request
import formcf

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("cf1.html")


@app.route("/user/<name>",methods=["GET","POST"])
def index2 (name="uno"):
    comment = formcf.CommentForm(request.form)
    if request.method == "POST":
        print (comment.username.data)
        print (comment.email.data)
        print (comment.comment.data)
    title="uno"
    edad = 18
    my_list = [1,2,3,4]
    return render_template("cf2.html",nombre=name,edad=edad,list=my_list,title=title, Form=comment)

if __name__ == "__main__":
    app.run(debug=True,port=5000)