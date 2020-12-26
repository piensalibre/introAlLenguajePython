#codigo 47, ejemplo de try/except
numero = input("Ingresa un numero entero positivo: ")
try:
    numero = int(numero)
except:
    numero = -1
if numero > 0:
    print("Buen trabajo")
else:
    print("No es un numero entero positivo")