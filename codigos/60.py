#codigo 60, ejemplo de codigo que encuentra al menor en una lista dada
menor = None
print("Al inicio")
for valor in [7,5,4,8,8,4,4,3,1,3,5,8,2,7,3]:
    if menor is None:
        menor = valor
    elif menor > valor:
        menor = valor
    print(menor,valor)
print("Al final")