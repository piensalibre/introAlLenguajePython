#codigo 122, ejemplo de codigo que extrae cadenas regulares
import re
linea = 'De: piensa@libre para ti'
x = re.findall('^De: .*@([^ ]*)',linea)
print(x)