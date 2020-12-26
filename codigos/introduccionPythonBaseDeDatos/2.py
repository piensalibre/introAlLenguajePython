#codigo 2, ejemplo de como mostrar el script que creo la base de datos
import mysql.connector

miBaseDeDatos = mysql.connector.connect(
    host = "localhost",
    user = "piensa",
    password = "piensa",
    database = "prueba"
)

cursor = miBaseDeDatos.cursor()

cursor.execute("show create table Usuario")#pedimos el script que se utilizo para crear la tabla

resultado = cursor.fetchall()

print(resultado)
