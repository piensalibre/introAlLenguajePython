#codigo 110, ejemplo de uso de expresiones regulares
import re
archivo = open("archivoDeTexto.txt")
for linea in archivo:
    linea = linea.rstrip()
    if re.search("hola", linea):#si se encuentra una vez la palabra hola se ejecuta el siguiente codigo
        print(linea)