#codigo 3, insertar datos a base de datos
import mysql.connector

miBaseDeDatos = mysql.connector.connect(
    host = "localhost",
    user = "piensa",
    password = "piensa",
    database = "prueba"
)

cursor = miBaseDeDatos.cursor()

sql = "insert into Usuario (email,username,edad) values (%s,%s,%s)"#creamos una variable que guarde la consulta, hacemos uso de "%s" para despues reemplazar los valores

values = ("micorreodesdepython","miusuario",22)#creamos una tupla con los valores a reemplazar

cursor.execute(sql,values)#pasamos como argumentos la consulta y los valores

miBaseDeDatos.commit()#ejecutamos la consulta de cursos.execute
