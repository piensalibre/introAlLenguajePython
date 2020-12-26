#codigo 57, ejemplo de for que da el promedio de los valores de la lista de numeros
contador = 0
suma = 0
print("Al inicio", contador,suma)
for valor in [3,4,2,4,7,7,8,8,6,7,7,7]:
    contador = contador + 1
    suma = suma + valor
    print(contador,suma,valor)
print("Al final",contador,suma,suma/contador)