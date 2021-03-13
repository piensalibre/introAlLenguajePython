#codigo 149, repaso
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad =edad
Persona.nombre = "Juan"
Persona.edad = 28
print(Persona.nombre)
print(Persona.edad)

persona = Persona("Pepe",15)
print(persona.nombre)
print(persona.edad)
print(id(persona))

otro = Persona("Paco",16)
print(otro.nombre)
print(otro.edad)
print(id(otro))