#codigo 74, ejemplo de uso de metodos de la clase str,se busca separar el dominio de un supuesto correo
cadena = "De piensalibre@holamundo.com jueves 17 de diciembre"
posicionInicial = cadena.find("@")
posicionFinal = cadena.find(" ",posicionInicial)
print(cadena[posicionInicial+1:posicionFinal])