from flask import Flask,render_template


app = Flask(__name__)

@app.route("/")
def index():
    return render_template("cf1.html")


@app.route("/user/<name>")
def index2 (name="uno"):
    edad = 18
    my_list = [1,2,3,4]
    return render_template("cf1.html",nombre=name,edad=edad,list=my_list)

if __name__ == "__main__":
    app.run(debug=True,port=5000)