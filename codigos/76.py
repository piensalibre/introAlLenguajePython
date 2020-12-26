#codigo 76, ejemplo de codigo que lee un archivo y cuenta las lineas del archivo usando el loop for
archivo = open("archivoDeTexto.txt")
cuenta = 0
for linea in archivo:
    cuenta = cuenta + 1
print("El archivo contiene",cuenta,"lineas")