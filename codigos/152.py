#codigo 152, repaso
class Caja:
    def __init__(self,largo,ancho,alto):
        self.largo = largo
        self.ancho = ancho
        self.alto = alto
    def calcularVolumen(self):
        return self.largo*self.alto*self.ancho
largo = int(input("Ingresa el largo: "))
ancho = int(input("Ingresa el ancho: "))
alto = int(input("Ingresa el alto: "))
cajita = Caja(largo,ancho, alto)
print(cajita.calcularVolumen())