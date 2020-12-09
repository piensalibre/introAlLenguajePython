#codigo 44, ejemplo de funcion que recibe numeros hasta que el usuario ya no quiera ingresar mas
lista = []

print("Ingrese numeros y para salir escriba la palabra salir")

while True:
    valor = input("Ingrese valor: ")
    if valor == "salir":
        break
    else:
        try:
            valor = int(valor)
            lista.append(valor)
        except:
            print("Dato invalido")
            exit()
resultado = 0

for x in lista:
    resultado += x
print(resultado)