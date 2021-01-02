#codigo 114, ejemplo de codigo que imprime una lista de cadenas que coinciden con la busqueda usando expresiones regulares, la lista tambien puede estar llena
import re
x = "Hola soy Piensa libre y mis numeros favoritos son el 7, el 21 y el 23"
y = re.findall('[0-9]+',x)
print(y)
y = re.findall('[AEIOU]+',x)
print(y)
