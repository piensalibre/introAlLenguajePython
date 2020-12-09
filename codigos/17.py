#codigo 17, ejemplo de validacion con el try-except en un programa que suma dos numeros
primero = input("Igresa un numero: ")
try:
    primero = int(primero)
except:
    primero = "Error"

if primero == "Error":
    print("Ingresaste mal el primer dato")
    exit()

segundo = input("Ingresa el segundo numero: ")
try:
    segundo = int(segundo)
except:
    segundo = "Error"

if segundo == "Error":
    print("Ingresaste mal el segundo dato")
    exit()

print(primero + segundo)
