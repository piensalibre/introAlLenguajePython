#codigo 91, ejemplo del metodo split, el cual convierte un string en una lista de strings
palabras = "Hola mundo Piensa libre"
print(palabras)
lista = palabras.split()
print(lista)
print(len(lista))
print(lista[0])
for palabra in lista:
    print(palabra)