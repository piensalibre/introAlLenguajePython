#codigo 59,ejemplo de codigo que busca el numero 3 dentro de una lista mediante un for loop
encontrado = False
print("Al inicio",encontrado)
for valor in [4,4,5,4,7,8,9,8,7,6,3,4,7]:
    if valor == 3:
        encontrado = True
        print(encontrado,valor)
        break
    print(encontrado,valor)
print("Al final",encontrado)