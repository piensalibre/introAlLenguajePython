#codigo 157, repaso
class Vehiculo():
    def __init__(self,color,ruedas):
        self.color = color
        self.ruedas = ruedas

    def __str__(self):
        return "El color del vehiculo es: "+self.color+"\nEl numero de ruedas es: "+str(self.ruedas)
    
class Coche(Vehiculo):
    def __init__(self, color, ruedas, velocidad):
        super().__init__(color, ruedas)
        self.velocidad = velocidad

    def __str__(self):
        return super().__str__()+"\nLa velocidad es: " + str(self.velocidad)

class Bici(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        super().__init__(color, ruedas)
        self.tipo = tipo

    def __str__(self):
        return super().__str__()+"\nEl tipo es: " + self.tipo

vehiculo = Vehiculo("verde",4)
coche = Coche("rojo",4,100)
bici = Bici("azul", 2, "montana")
print(vehiculo)
print()
print(coche)
print()
print(bici)
