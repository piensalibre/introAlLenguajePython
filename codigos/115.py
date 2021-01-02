#codigo 115, ejemplo de impresion de cadenas usando expresiones regulares, en este caso se muestra como el uso de * y + buscan la cadena mas larga posible
import re
x = "Desde: Usando : dos veces para demostrar como funcionan el * y el + y buscan la cadena mas larga"
y = re.findall('^D.+:',x)
print(y)