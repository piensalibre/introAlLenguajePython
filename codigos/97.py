#codigo 97, ejemplo de uso de diccionarios y de su metodo get
cuenta = {}
nombres = ["Piensa","libre","Hola","mundo","libre"]
for nombre in nombres:
    cuenta[nombre] = cuenta.get(nombre,0) +1
print(cuenta)