#codigo 112,ejemplo de codigo que imprime lineas de un archivo que empiezan con una palabra especifica usando expresiones regulares
import re
archivo = open("archivoDeTexto.txt")
for lineas in archivo:
    lineas = lineas.rstrip()
    if re.search("^un",lineas):#el caracter '^' indica que la cadena debe encontrarse al inicio de la linea
        print(lineas)