#codigo 118, ejemplo de uso de paranresis para delimitar que porcion de la cadena extraer, los parentesis no son parte de la busqueda
import re
x = 'De: piensa@libre.com para ti'
y = re.findall('^De: (\S+@\S+)',x)
print(y)