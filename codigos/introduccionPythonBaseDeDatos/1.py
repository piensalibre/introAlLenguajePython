#codigo 1, ejemplo de creacion de conexion y de cursor para interactuar con python
import mysql.connector#se importa el conector previamente instalado con el comando de terminal "pip3 install mysql-connector-python"
miBaseDeDatos = mysql.connector.connect(#se crea la variable miBaseDeDatos que recibe la conexion del metodo connector.connect, este metodo recibe 4 argumentos, el host que es donde nos vamos a conectar, user que es el usuario, password que es la contrasena y database que es el nombre de la base de datos
    host = "localhost",
    user = "piensa",
    password = "piensa",
    database = "prueba"
)

cursor = miBaseDeDatos.cursor()#el cursor nos permitira interactuar con la base de datos mediante lenguaje sql

cursor.execute("select * from Usuario")#el metodo execute nos permite pasarle consultas sql

resultado = cursor.fetchall()#creamos la variable resultado que recibira todos los elementos que se encontraron en la base de datos gracias al metodo fetchall

print(resultado)#imprimimos la variable resultado
