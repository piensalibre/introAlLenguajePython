#codigo 77, ejemplo de uso del metodo read, este metodo no es recomendable para archivos grandes
archivo = open("archivoDeTexto.txt")
lector = archivo.read()
print("El siguiente archivo tiene",len(lector),"letras")
print(lector)