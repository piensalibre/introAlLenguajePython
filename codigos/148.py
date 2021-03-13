#codigo 148, repaso
def miFuncion():
    print("Ejecutando mi funcion")

miFuncion()

def funcionArgumentos(nombre):
    print("El nombre recibido es: ", nombre)

funcionArgumentos("Piensa")

def suma(a=0,b=0):
    return a + b

print(suma(5,7))