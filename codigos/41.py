#codigo 41,funcion que define si un usuario es mayor de edad
def esMayor(usuario):
    return usuario.edad > 17

class Usuario:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad

usuario = Usuario("Piensa",27)
usuario2 = Usuario("libre",7)

res = esMayor(usuario)
res2 = esMayor(usuario2)

print(res,res2)