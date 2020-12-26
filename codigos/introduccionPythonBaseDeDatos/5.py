#codigo 5, ejemplo de eliminar datos de base de datos
import mysql.connector

miBaseDeDatos = mysql.connector.connect(
    host = "localhost",
    user = "piensa",
    password = "piensa",
    database = "prueba"
)

cursor = miBaseDeDatos.cursor()

sql = "delete from Usuario where id = %s"

values = (3,)#a pesar de solo ser un valor a reemplazar se debe enviar como una tupla, notese la ',' despues del valor

cursor.execute(sql,values)

miBaseDeDatos.commit()
