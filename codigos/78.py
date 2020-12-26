#codigo 78, ejemplo de codigo que busca un prefijo en una linea
archivo = open("archivoDeTexto.txt")
for linea in archivo:
    if linea.startswith("un"):
        print(linea)