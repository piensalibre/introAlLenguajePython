#codigo 155, repaso
class Persona:
    def __init__(self,nombre,apellidoP,apellidoM):
        self.nombre = nombre
        self._apellidoP = apellidoP
        self.__apellidoM = apellidoM
    def metodoPublico(self):
        self.__metodoPrivado()

    def __metodoPrivado(self):
        print(self.nombre)
        print(self._apellidoP)
        print(self.__apellidoM)

    def getNombre(self):
        return self.nombre

    def getApellidoMaterno(self):
        return self.__apellidoM

    def getApellidoPaterno(self):
        return self._apellidoP

    def setNombre(self,nombre):
        self.nombre = nombre

    def setApellidoMaterno(self,apellidoM):
        self.__apellidoM = apellidoM

    def setApellidoPaterno(self,apellidoP):
        self._ApellidoP = apellidoP

p1 = Persona("Pepe","Lopez","Perez")
p1.metodoPublico()
print(p1.nombre)
print(p1._apellidoP)#atributo semiprivado
#print(p1.__apellidoM)atributo privado
print(p1.getApellidoMaterno())