#codigo 116, ejemplo de como usar el caracter '?' para delimitar a buscar la cadena mas corta
import re
x = 'Desde: usamos : dos veces para demostrar como podemos con el caracter ? buscar la cadena mas corta'
y = re.findall('^D.+?:',x)
print(y)