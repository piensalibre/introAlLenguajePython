#codigo 90, ejemplo de uso de algunas funciones que interactuan con las listas
lista = []
while True:
    num = input("Escribe 'listo' para dejar de ingresar numeros o ingresa un numero: ")
    if num == "listo":
        break
    try:
        numero = float(num)
    except:
        print("No elegiste una opcion valida, intenta de nuevo.")
        continue
    lista.append(numero)
promedio = sum(lista)/len(lista)
print("Ingresaste",len(lista),"numeros y el promedio de dichos numeros es",promedio)