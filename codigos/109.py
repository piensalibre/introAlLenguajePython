#codigo 109, ejemplo de buscar dentro de un archivo
archivo = open("archivoDeTexto.txt")
for lineas in archivo:
    lineas = lineas.rstrip()
    if lineas.find("hola") >= 0:
        print(lineas)
