#codigo 24, ejemplo de clases y objetos
class Usuario:#se indica la definicion de una clase mediante la palabra definida class, y el nombre de la clase, por convencion la primera letra de la clase se escribe en mayuscula
    nombre = "Piensa"#nombre es una propiedad de la clase Usuario
    apellido = "libre"
usuario = Usuario()#se crea el objeto de la clase Usuario

print(usuario.nombre)#se acceda a la propiedad mediante el uso de '.'
print(usuario.apellido)