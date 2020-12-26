#codigo 99, ejemplo de impresion de diccionarios
diccionario = {"uno":1,'dos':2,"tres":3}
for llave in diccionario:
    print(llave,diccionario[llave])
print(list(diccionario))
print(list(diccionario.keys()))
print(list(diccionario.values()))
print(list(diccionario.items()))