from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return "Hola mundo"
    
@app.route("/params")
def params():
    params = request.args.get('uno',"no contiene este parametro")
    paramsDos = request.args.get("dos", "no contiene parametro")
    return "El parametro es: {},{}".format(params, paramsDos)

if __name__ =="__main__":
    app.run(debug = True, port = 5000)