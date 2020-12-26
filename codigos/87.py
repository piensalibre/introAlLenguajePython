#codigo 87, ejemplo de uso de los operadores in y not in en las listas
lista = []
lista.append("Piensa")
lista.append("libre")
lista.append("Hola")
lista.append("mundo")
if "Hola" in lista:
    print("Si esta la palabra 'Hola'")
if "adios" not in lista:
    print("No esta la palabra 'adios'")