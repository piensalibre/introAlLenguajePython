#codigo 25, ejemplo de objetos y clases
class Usuario:
    def __init__(self, nombre, apellido):#la funcion __init__ es la que se ejecutara al momento de ser creada la instancia de la clase Usuario, recibe como primer parametro la palabra reservada self la cual indica que se esta llamando al objeto en si
        self.nombre = nombre
        self.apellido = apellido

usuario = Usuario("Piensa","libre")#la instancia esta recibiendo las cadenas las cuales utilizara despues en el metodo __init__
usuario2 = Usuario("Hola","mundo")

print(usuario.nombre,usuario.apellido)
print(usuario2.nombre,usuario2.apellido)