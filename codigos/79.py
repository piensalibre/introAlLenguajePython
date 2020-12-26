#codigo 79, ejemplo de codigo que imprime las lineas de un archivo sin el ultimo \n para que solo se agregue el \n de la funcion print y la impresion en pantalla no tenga lineas vacias extras 
archivo = open("archivoDeTexto.txt")
for linea in archivo:
    print(linea.rstrip())