#codigo 130,repaso
a = int(input("Ingresa un valor "))
valorMinimo = 0
valorMaximo = 5
dentroRango = a >= valorMinimo and a <= valorMaximo
if dentroRango:
    print("Dentro de rango")
else:
    print("Fuera de rango")


vacaciones = False
diaDescanso = True
if vacaciones or diaDescanso:
    print("Ir al parque")
else:
    print("No es posible ir al parque")

print(vacaciones)
print(not(vacaciones))