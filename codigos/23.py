#codigo 23, ejemplo de funciones y recursividad
def recursion(i):
    if (i < 1):
        return i
    print(i)
    recursion(i - 1)#la funcion se llama a si misma

recursion(20)