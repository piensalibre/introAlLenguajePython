#codigo 61, ejemplo de codigo que recorre una cadena e imprime las letras de esta mediante un indice dentro de un while
palabra = "Hola"
indice = 0
while indice < len(palabra):
    letra = palabra[indice]
    print(indice, letra)
    indice = indice + 1