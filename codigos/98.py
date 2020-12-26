#codigo 98, ejemplo de codigo que cuenta las palabras de una linea de texto
cuenta = {}
linea = input("Ingresa una linea de texto: ")
palabras = linea.split()
print(palabras)
for palabra in palabras:
    cuenta[palabra] = cuenta.get(palabra,0) + 1
print(cuenta)