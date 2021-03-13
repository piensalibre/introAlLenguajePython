#codigo 162
class MiClase:
    variableClase = "Variable de clase inicial"
    def __init__(self,variableInstancia):
        self.variableInstancia = variableInstancia
print(MiClase.variableClase)
objeto1 = MiClase("uno")
objeto2 = MiClase("dos")
print(objeto1.variableInstancia)
print(objeto2.variableInstancia)
MiClase.variableClase="Variable de clase modificada"
print(MiClase.variableClase)
print(objeto1.variableClase)
print(objeto2.variableClase)
MiClase.variableClase="Variable de clase modificada2"
print(MiClase.variableClase)
print(objeto1.variableClase)
print(objeto2.variableClase)