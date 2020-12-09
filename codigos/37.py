#codigo 37, ejercicio que multiplica dos numeros sin usar el simbolo de multiplicacion
resultado = 0
x = input("Ingresa el primer numero: ")

try:
    x = int(x)
except:
    x = "Error"

if x == "Error":
    print("Ingresaste mal el primer dato")
    exit()

y = input("Ingresa el segundo numero: ") 

try:
    y = int(y)
except:
    y = "Error"

if y == "Error":
    print("Ingresaste mal el segundo dato")
    exit()

for a in range(x):
    resultado += y

print(resultado)