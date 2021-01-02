#codigo 121, ejemplo de como extraer cadenas usando expresiones regulares
import re
x = 'De piensa@libre para ti'
y = re.findall('@([^ ]*)',x)#'^ ' indica un set de caracteres que no tengan un espacio en blanco
print(y)