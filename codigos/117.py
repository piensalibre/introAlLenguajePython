#codigo 117, otro ejemplo de como extraer partes de una cadena con expresiones regulares
import re
x = 'De: piensa@libre.com para ti'
y = re.findall('\S+@\S+',x)#va a buscar cadenas sin espacios con uno o mas caracteres a la derecha y a la izquierda
print(y)