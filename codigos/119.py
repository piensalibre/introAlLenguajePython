#codigo 119, ejemplo de como extraer cadenas usando find y slicing de cadenas
x = 'De: piensa@libre para ti'
posInicial = x.find('@')
posFinal = x.find(' ',posInicial)
host = x[posInicial+1:posFinal]
print(host)