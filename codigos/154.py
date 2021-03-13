#codigo 154, repaso
class Persona:
    def __init__(self,nombre,edad):        
        self.__nombre = nombre
        self.__edad = edad
    
    def getNombre(self):
        return self.__nombre

    def setNombre(self, nombre):
        self.__nombre = nombre

    def getEdad(self):
        return self.__edad

    def setEdad(self, edad):
        self.__edad = edad

p1 = Persona("Pepe",20)
print(p1.getNombre())
print(p1.getEdad())
p1.setNombre("Paco")
p1.setEdad(40)
print(p1.getNombre())
print(p1.getEdad())