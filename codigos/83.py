#codigo 83, ejemplo de codigo que recibe el nombre de un archivo y pone el manejador del archivo en un try/except por si no logra abrirlo
nombreDelArchivo = input("Ingresa el nombre del archivo: ")
try:
    archivo = open(nombreDelArchivo)
except:
    print("No existe un archivo con ese nombre")
    quit()
count = 0
for linea in archivo:
    if linea.startswith("un"):
        count = count + 1
print("En el archivo hay",count,"lineas que empiezan con 'un'")