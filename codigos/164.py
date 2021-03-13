#164.py
class MiClase:
    
    variableClase = "Variable clase"
    
    def __init__(self):
        self.variableInstancia = "Variable instancia"

    @staticmethod
    def metodoStatico():
        print("Metodo estatico")
        print(MiClase.variableClase)

    @classmethod
    def metodoClase(cls):
        print("Metodo de clase"+str(cls))
        print(cls.variableClase)

    def metodoInstancia(self):
        self.metodoStatico()
        self.metodoClase()
        print(self.variableClase)
        print(self.variableInstancia)


MiClase.metodoStatico()
MiClase.metodoClase()
print()
objeto = MiClase()
objeto.metodoInstancia()