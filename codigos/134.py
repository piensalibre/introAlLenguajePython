#codigo 134, repaso
condicion = True
if condicion == True:
    print("La condicion es verdadera")
elif condicion == False:
    print("La condicion es falsa")
else:
    print("Condicion no reconocida")

numero = int(input("Introduzca un numero entre 1 y 3: "))
if numero == 1:
    numeroTexto = "Numero 1"
elif numero == 2:
    numeroTexto = "Numero 2"
elif numero == 3:
    numeroTexto = "Numero 3"
else:
    numeroTexto = "Numero fuera de rango"
print("El numero proporcionado es "+ numeroTexto)
