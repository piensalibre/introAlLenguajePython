#octavo codigo, empezamos a usar diccionarios

diccionario = {
        "nombre":"Piensa",
        "apellido":"Libre",
        "edad":31
        }#definimos la variable diccionario de tipo diccionario, esto se define con valores bajo el esquema llave:valor encerrados entre {}, cada valor es separado por comas
print(diccionario)

print(diccionario["nombre"])#se imprime el valor especifico que de llama mediante la llave encerrada entre corchetes

print(diccionario["apellido"])

print(diccionario["edad"])

print(diccionario.get("nombre"))#se obtiene el valor mediante el metodo get()

print(diccionario.get("apellido"))

print(diccionario.get("edad"))

diccionario["edad"] = 32#se asigna el valor de manera directa al elemento del diccionario mediante la llave encerrada dentro de corchetes con el operador = que precede a; nuevo valor

print(diccionario["edad"])

print(len(diccionario))#se utiliza la funcion len para obtener el tamano del diccionario

diccionario["nacionalidad"] = "mexicano"#se agrega una nueva llave mediante el nombre de dicha llave dentro de corchetes seguido del operador de asignacion y el valor que se le queire dar a la llave

print(diccionario)

diccionario.pop("edad")#el metodo pop elimina la llave pasada a la funcion dentro de los parentesis

print(diccionario)

diccionario.popitem()#elimina la ultima llave agregada al diccionario

print(diccionario)

del diccionario["nombre"]#la funcion del elimina la llave del diccionario que aparece entre corchetes

print(diccionario)

copiaDiccionario = diccionario.copy()#se copia el diccionario a copiaDiccionario mediante el metodo copy

print(copiaDiccionario)

diccionario.clear()#se vacia el diccionario

print(diccionario)

diccionario2 = dict(copiaDiccionario)#se asigna el diccionario copiaDiccionario a la variable diccionario2 mediante la funcion dict

print(copiaDiccionario)

print(diccionario2)
