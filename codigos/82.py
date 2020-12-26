#codigo 82, ejemplo de codigo que pide al usuario que ingrese el nombre del archivo
nombreDelArchivo = input("Ingresa el nombre del archivo: ")
archivo = open(nombreDelArchivo)
cuenta = 0
for linea in archivo:
    if linea.startswith("un"):
        cuenta = cuenta + 1
print("Se encontraron",cuenta,"lineas que empezaban con 'un'")