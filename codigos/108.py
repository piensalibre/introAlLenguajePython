#codigo 108, ejemplo de contar palabras de un archivo de texto e imprimir las 5 palabras que mas se repiten
archivo = open('archivoDeTexto.txt')
diccionario = dict()
for lineas in archivo:
    lineas = lineas.rstrip()
    palabras = lineas.split()
    for palabra in palabras:
        diccionario[palabra] = diccionario.get(palabra,0) + 1

temp = list()
for k,v in diccionario.items():
    tupla = (v,k)
    temp.append(tupla)
temp = sorted(temp, reverse=True)    
for v,k in temp[:5]:
    print(k,v)