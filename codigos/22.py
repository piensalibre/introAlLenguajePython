#codigo 22, ejemplo de funciones
def miFuncion():#se utiliza la palabra reservada def para definir funciones, seguida de parentesis y ':' para ejecutar el bloque de codigo que sigue
    print("Mi primer funcion")

miFuncion()

def imprimeDato(argumentoUno):#la funcion recibira como argumento lo que se le pase a la funcion dentro de esos parentesis
    print("Mi argumento es",argumentoUno)

imprimeDato("parametro")#se le pasa el parametro a la funcion

def imprimeNombre(nombre,apellido):#las funciones pueden recibir mas de un argumento
    print("El nombre completo es:",nombre, apellido)

imprimeNombre("Piensa","libre")

def imprimeNombre2(*nombre):#el * indica que la funcion puede recibir como argumento una tupla
    print("El nombre completo es:",nombre)

imprimeNombre2("Piensa","libre")

def nombreCompleto(apellido, nombre):
    print(nombre, apellido)

nombreCompleto(nombre = "Piensa", apellido = "libre")#se accede a los argumentos de la funcion asignandole por medio del operador '=' el valor

def nombreCompleto2(**kwargs):#paso de argumentos utilizando los keywordargs
    print(kwargs['nombre'], kwargs['apellido'])

nombreCompleto2(nombre = "Piensa",apellido = "libre")

def nombreCompleto3(nombre = "Piensa", apellido = "libre"):#paso de argumentos por defecto
    print(nombre, apellido)

nombreCompleto3()

def miFuncionLista(lista):#una funcion puede recibir como argumentos listas
    for elemento in lista:
        print(elemento)

miFuncionLista(["Piensa","libre"])

def concatenaNombres(lista):
    i = ""
    for el in lista:
        i = i + el + " "
    return i#una funcion puede retornar un valor

nombres = concatenaNombres(["Piensa","libre"])

print(nombres)