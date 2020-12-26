#codigo 106, codigo que imprime las 10 palabras que mas se repiten en un archivo
archivo = open("archivoDeTexto.txt")
contador = {}
for lineas in archivo:
    palabras = lineas.split()
    for palabra in palabras:
        contador[palabra] = contador.get(palabra,0) + 1
lista = []
for llave,valor in contador.items():
    lista.append((valor,llave))
lista = sorted(lista,reverse=True)
for valor,llave in lista[:10]:
    print(llave,valor)