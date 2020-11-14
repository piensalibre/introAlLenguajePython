#quinto codigo, se muestra el uso de listas

lista = []#se declara una lista vacia

print(lista)#se imprime la lista vacia

lista2 = [1,2,3]#se declara una lista2

print(lista2)#se imprime la lista2

lista2.append(4)#agrega un elemento al final con el metodo append

print(lista2)

lista2.clear()#este metodo borra la lista

print(lista2)

lista2 = [1,2,3]#se declara una lista2

lista3 = lista2.copy()#se copia lista2 a lista3

print(lista3)

print(lista2.count(2))#El metodo count cuenta el numero de veces que se repite un elemento2

print(len(lista2))#La funcion len indica el largo de la lista que se le pasa

largoLista2 = len(lista2)#se crea variable largoLista2 y se le asigna el valor del largo de lista2

print(largoLista2)

print(lista2[0])#se imprime en pantalla el primer elemento de lista2 agregando entre los corchetes el numero correspondiente al indice, en python el indice de elementos inicia en 0

lista4 = ["Hola","mundo","jejeje"]

print(lista4)

lista4.pop()#elimina el ultimo elemento de lista 4

print(lista4)

lista4.append("jojojo")

print(lista4)

lista4.remove("mundo")#este metodo remueve un elemento espesifico

print(lista4)

lista4.reverse()#cambia el orden de la lista de manera inversa

print(lista4)

lista4.sort()#metodo que ordena los elementos de la lista siempre y cuando tengan el mismo tipo de dato

print(lista4)
