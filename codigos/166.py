#codigo 166
class Persona:
    def __init__(self,nombre):
        self.__nombre=nombre

    def __add__(self,otro):
        return self.__nombre + " " + otro.__nombre
        
a = 1
b = 2
print(a+b)

st1 = "Hola "
st2 = "mundo"
print(st1+st2)

list1=[1,2]
list2=[3,4]
print(list1+list2)
p1 = Persona("uno")
p2 = Persona("dos")
print(p1+p2)
