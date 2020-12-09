#codigo 29, ejercicio de herencia
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido

    def saludo(self):
        print("Hola mi nombre es",self.nombre,self.apellido)

class Admin(Usuario):
    def superSaludo(self):
        print("Hola mi nombre es",self.nombre," y soy administrador.")

class Mascota:
    def __init__(self,nombre,sonido):
        self.nombre = nombre
        self.sonido = sonido

    def saludo(self):
        print("Hola soy un",self.tipo," y mi sonido es el",self.sonido)

class Gato(Mascota):
    tipo = "gato"

class Perro(Mascota):
    tipo = "perro"

gato = Gato("Bicho","maullido")
gato.saludo()

perro = Perro("Puppy","ladrido")
perro.saludo()