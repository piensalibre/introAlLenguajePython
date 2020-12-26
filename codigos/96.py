#codigo 96,ejemplo de uso de diccionario para contar
diccionario = {}
nombres = ["Piensa","libre","Hola","mundo","Piensa","libre","libre"]
for nombre in nombres:
    if nombre not in diccionario:
        diccionario[nombre] = 1
    else:
        diccionario[nombre] = diccionario[nombre] + 1
print(diccionario)