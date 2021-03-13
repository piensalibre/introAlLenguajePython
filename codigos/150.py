#codigo 150, repaso
class Aritmetica:
    def __init__(self, operando1, operando2):
        self.operando1 = operando1
        self.operando2 = operando2

    def sumar(self):
        """Se realiza una suma dentro de la clase aritmetica"""
        return self.operando1 + self.operando2
    
suma1 = Aritmetica(5,4)

print(suma1.sumar())