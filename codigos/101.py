#codigo 101, ejemplo de codigo que pide el nombre de un archivo, lo lee separa las palabras de cada linea guardandolas en una lista, luego itera la lista con un for y cuenta las palabras almacenando el resultado en un diccionario, despues mediante un for itera el diccionario usando dos variables y asigna la palabra que mas se repite y su numero a dos variables que luego se imprimen como el resultado final
nombre = input("Ingresa el nombre del archivo: ")
archivo = open(nombre)
cuenta = {}
for linea in archivo:
    palabras = linea.split()
    for palabra in palabras:
        cuenta[palabra] = cuenta.get(palabra,0) + 1
numero = None
letra = None
for palabra,contador in cuenta.items():
    if numero is None or contador > numero:
        letra = palabra
        numero = contador
print(letra,numero)