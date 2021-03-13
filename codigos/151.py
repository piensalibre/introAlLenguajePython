#codigo 151, repaso
class Rectangulo:
    def __init__(self,base,altura):
        self.base = base
        self.altura = altura
    def calcularArea(self):
        return self.base*self.altura
base = int(input("Ingrese la base: "))
altura = int(input("Ingrese la altura: "))
rec=Rectangulo(base,altura)
print(rec.calcularArea())