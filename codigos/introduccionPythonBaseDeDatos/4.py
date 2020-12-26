#codigo 4, ejemplo de actualizar base de datos
import mysql.connector

miBaseDeDatos = mysql.connector.connect(
    host = "localhost",
    user = "piensa",
    password = "piensa",
    database = "prueba"
)

cursor = miBaseDeDatos.cursor()

sql = "update Usuario set email = %s where id = %s"

values = ("micorreito", 4) 

cursor.execute(sql,values)

miBaseDeDatos.commit()
