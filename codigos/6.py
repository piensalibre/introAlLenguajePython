#sexto codigo, se usan las tuplas
tupla = ("Hola","mundo","somos","una","tupla")#tupla, tipo de lista que no puede ser modificada a lo largo del programa, a diferem=ncia de las listas esta usa parentesis en lugar de corchetes

print(tupla)

print(tupla.count("Hola"))#las tuplas tienen sus propios metodos, algunos similares a las listas, las tuplas aceptan el metodo count que regresa el numero de veces que la tupla contiene dicho elemento

print(tupla.index("Hola"))#este metodo regresa el indice que contiene dicho elemento

print(tupla[4])#imprime el elemento ubicado en la posicion marcada por el indice dentro de los corchetes

listaDeTupla = list(tupla)#con la funcion list se convierte la tupla a una lista para poder ser modificadadurante la ejecucion del programa

listaDeTupla.append("convertida a lista")#El metodo append grega un elemento a la lista listaDeTupla mas no la tupla tupla

print(listaDeTupla)

print(tupla)
