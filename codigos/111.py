#codigo 111, ejemplo de como imprimir lineas de un archivo que empiezan con una palabra
archivo = open("archivoDeTexto.txt")
for linea in archivo:
    linea = linea.rstrip()
    if linea.startswith("un"):
        print(linea)