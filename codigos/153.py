#codigo 153, repaso
class Persona:

    def __init__(self, nombre, edad, *v,**d):
        self.nombre = nombre
        self.edad = edad
        self.valores = v
        self.diccionario = d

    def desplegar(self):
        print("Nombre: ",self.nombre)
        print("Edad: ",self.edad)
        print("Valores pasados como tupla: ",self.valores)
        print("Valores pasados como diccionario: ",self.diccionario)

p1 = Persona("Piensa", 22)
print(p1.nombre)
print(p1.edad)
p1.desplegar()

print()

p2 = Persona("Piensa2", 33,2,3,4,5)
print(p2.nombre)
print(p2.edad)
p2.desplegar()
print()
p3 = Persona("Piensa3", 23,1,2,3, m="manzana",p="pera",j="jicama")
p3.desplegar()