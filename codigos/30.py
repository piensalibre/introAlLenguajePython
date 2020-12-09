#codigo 30, ejemplo para extender el metodo __init__
class Mascota:
    def __init__(self,nombre,sonido):
        self.nombre = nombre
        self.sonido = sonido
    
    def saludo(self):
        print("Hola soy un",self.tipo,"y mi sonido es",self.sonido)

class Gato(Mascota):
    tipo = "gato"
    def __init__(self,nombre,sonido):
        Mascota.__init__(self,nombre,sonido)#debido a que al definir el  metodo __init__ dentro de la clase gato ya no se va a ejecutar el metodo de la clase padre se debe incluir el metodo de manera explicita en el nuevo __init__ si es que se requiere
        print("Hola soy un mensaje de la clase gato que se ejecuta al crear una instancia de la clase gato")

class Perro(Mascota):
    tipo = "perro"
    def __init__(self,nombre,sonido):
        super().__init__(nombre,sonido)#otra manera de extender el metodo __init__ de la clase padre
        print("Mensaje desde la clase perro")

gato = Gato("Bicho","maullido")
gato.saludo()

perro = Perro("Puppy","ladrido")
perro.saludo()