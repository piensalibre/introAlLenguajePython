#codigo 55, ejemplo de iteracion con for que encuentra el numero mas grande
numeroMasGrande = 0
print("Al inicio",numeroMasGrande)
for numero in [3,5,2,4,6,2,12,43,56,33,77,32]:
    if numero > numeroMasGrande:
        numeroMasGrande = numero
    print(numeroMasGrande,numero)
print("Al final",numeroMasGrande)