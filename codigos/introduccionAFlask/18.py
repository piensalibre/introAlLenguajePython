from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "Hola"

@app.route("/params<uno>/")
@app.route("/params/<dos>")
@app.route("/params<int:uno>/<dos>")
def params(uno="valor por defecto",dos="valor por defecto"):
    return "El parametro es {}, {}".format(uno,dos)


if __name__ == "__main__":
    app.run(debug=True,port=5000)