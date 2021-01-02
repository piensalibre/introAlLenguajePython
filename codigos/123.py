#codigo 123, ejemplo de uso del caracter '\' para poder usar caracteres especiales como caracteres normales
import re
x = 'Nos dieron $10.00 pesos para galletas'
y = re.findall('\$[.0-9]+',x)#el caracter '\' hace que se busque al caracter '$' y le quita su significado como caracter especial dentro de las expresiones regulares
print(y)