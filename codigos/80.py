#codigo 80, codigo que se salta, las lineas que no cumplan la condicion
archivo = open("archivoDeTexto.txt")
for linea in archivo:
    linea = linea.rstrip()
    if not linea.startswith("s"):
        continue
    print(linea)