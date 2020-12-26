#codigo 81, codigo que filtra que imprimir usando "in"
archivo = open("archivoDeTexto.txt")
for linea in archivo:
    linea = linea.rstrip()
    if not "un" in linea:
        continue
    print(linea)