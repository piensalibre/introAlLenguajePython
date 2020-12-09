#codigo 45, funcion que recibe nombre y apellido y los agrega a un archivo
def agregaNombreArchivo(nombre,apellido):
    p = open("nombreCompleto.txt","a")
    p.write(nombre + " " + apellido + "\n")
    p.close()

agregaNombreArchivo("Piensa", "libre")
agregaNombreArchivo("Hola", "mundo")