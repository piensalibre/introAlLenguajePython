#codigo 26, ejemplo de clases y objetos
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    def saludo(self):#se crea un metodo que recibe como argumento la instancia misma
        print("Hola mi nombre es",self.nombre,self.apellido)

usuario = Usuario("Piensa","libre")
usuario2 = Usuario("Hola","mundo")

usuario.saludo()#para acceder a los metodos se hace uso de '.' al igual que cuando se accede a las propiedades
usuario2.saludo()