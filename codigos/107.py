#codigo 107, ejemplo de como imprimir los primeros 5 elementos de una lista en orden alfabetico con el valor de veces que se repiten dentro de un texto, si no se especifica un nombre de texto se usa el texto archivoDeTexto.txt
nombre = input('Ingresa el nombre del archivo: ')
if len(nombre) < 1:
    nombre = 'archivoDeTexto.txt'
manejador = open(nombre)

diccionario = dict()
for linea in manejador:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra, 0) + 1
print(diccionario)

x = sorted(diccionario.items())
print(x[:5])