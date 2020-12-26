#codigo 56, ejemplo de for loop que cuenta el numero de veces que se ejecuta el loop
contador = 0
print("Al inicio",contador)
for num in [1,3,5,2,5,6,7]:
    contador = contador + 1
    print(contador,num)
print("Al final",contador)