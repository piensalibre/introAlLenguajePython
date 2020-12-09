#codigo 28,ejemplo de herencia
class Usuario:
    def __init__(self,nombre,apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def saludo(self):
        print("Hola soy",self.nombre,self.apellido)

class Admin(Usuario):#se define la clase Admin y se le pasa la clase Usuario de la cual hereda los metodos y propiedades
    def superSaludo(self):
        print("Hola soy",self.nombre," y soy administrador")


usuario = Usuario("Piensa","libre")
admin = Admin("Hola","mundo")

usuario.saludo()
admin.saludo()
admin.superSaludo()