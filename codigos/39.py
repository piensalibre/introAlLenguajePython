#codigo 39, ejercicio de una funcion que encuetra el menor de una lista
lista = [1,2,19,-83,44,2,-2,-24,-55]

menor = "inicial"

for x in lista:
    if menor == "inicial":
        menor = x
    else:
        menor = x if x < menor else menor

print("menor",menor)