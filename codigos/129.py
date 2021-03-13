#codigo 129, repaso
a = 5
b = 3
resultado = a == b
print(resultado)
resultado = a != b
print(resultado)
resultado = a > b
print(resultado)
resultado = a < b
print(resultado)
resultado = a >= b
print(resultado)
resultado = a <= b
print(resultado)

if (a%2==0):
    print("Es un numero par")
else:
    print("Es impar")

edadLimite = 18
edad = int(input("ingresa tu edad "))
if edad >= edadLimite:
    print("Es mayor de edad")
else:
    print("Es menor de edad")