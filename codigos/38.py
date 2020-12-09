#codigo 38, ejercicio que recibe nombre y apellido y lo imprime al reves
nombre = input("Ingresa tu nombre: ")
apellido = input("Ingresa tu apellido: ")

concatenacion = nombre + " " + apellido

print(concatenacion[::-1])