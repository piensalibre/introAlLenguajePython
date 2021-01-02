#codigo 113, uso de expresiones regulares para extraer cadenas de otras cadenas
import re
x = 'Mis numero favoritos son el 7, el 21 y el 23'
y = re.findall('[0-9]+',x)#findall devuelve como una lista las cadenas que coinciden, en este caso es un rango de incluye cualquier digito que se repite una o mas veces
print(y)