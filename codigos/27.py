#codigo 27, ejemplo uso de clases y objetos
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print("Hola soy",self.nombre,self.apellido)

usuario = Usuario("Piensa","libre")

usuario.saludo()

usuario.nombre = "Hola"#se puede modificar las propiedades de manera directa asignando un nuevo valor mediante el operador '='

usuario.saludo()

