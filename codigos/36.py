#codigo 36, ejemplo de uso de la libreria os y de como borrar archivos
import os

p = open("texto.txt","w")

p.write("Hola mundo\n")

p.close()

if os.path.exists("texto.txt"):#se verifica si el archivo existe
    os.remove("texto.txt")#se elimna el archivo cuyo nombre se encuentra dentro de los parentesis, si fuera un directorio el que se quisiera eliminar se utiliza el metodo "os.rmdir()""
else:
    print("El archivo no existe")