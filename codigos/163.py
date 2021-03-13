#codigo 163
class MiClase:
    variableClase = "Variable de clase"
    def __init__(self,variableInstancia):
        self.variableInstancia=variableInstancia
print(MiClase.variableClase)
objeto1 = MiClase("Variable de instancia del objeto")
MiClase.variableInstancia = "Modificando la variable de instancia en la clase"
print(MiClase.variableInstancia)
print(objeto1.variableInstancia)
print(objeto1.variableClase)
print(MiClase.variableClase)
objeto1.variableClase="Variable clase modificada desde el objeto"
print(objeto1.variableClase)
print(MiClase.variableClase)
objeto2 = MiClase("Variable de instancia2")
print(objeto2.variableInstancia)
print(objeto2.variableClase)
MiClase.variableClase="Cambio desde la clase"
print(MiClase.variableClase)
print(objeto1.variableClase)
print(objeto2.variableClase)