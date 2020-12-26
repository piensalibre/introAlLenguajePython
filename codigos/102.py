#codigo 102, codigo que lee un archivo y cuenta las palabras y dice cual es la que mas se repite
nombre = input("Ingresa el nombre del archivo: ")
try:
    archivo = open(nombre)
except:
    print("No se puede leer el archivo")
    exit()
diccionario = {}
for linea in archivo:
    linea = linea.rstrip()
    palabras = linea.split()
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra,0) + 1
contador = None
palabra = None
for llave,valor in diccionario.items():
    if contador is None or valor > contador:
        contador = valor
        palabra = llave
print("La palabra",palabra,"se repite",contador,"veces")