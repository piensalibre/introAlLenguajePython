#codigo 147, repaso
diccionario = {
    "IDE":"Entorno de desarrollo",
    "OOP":"Programacion orientada a objetos",
    "DBMS":"Sistema manejador de base de datos"
}
print(diccionario)
print(len(diccionario))
print(diccionario["IDE"])
print(diccionario.get("IDE"))
diccionario["IDE"]="Entorno"
print(diccionario.get("IDE"))
for llave in diccionario:
    print(llave) 
for llave in diccionario:
    print(diccionario[llave])
for valor in diccionario.values():
    print(valor)
for valor in diccionario.items():
    print(valor)
for key,valor in diccionario.items():
    print(key)
for key,valor in diccionario.items():
    print(valor)
for key,valor in diccionario.items():
    print("Llave y valor")
    print(key)
    print(valor)
print("IDE" in diccionario)
diccionario["PK"] = "Primary key"
print(diccionario
)
diccionario.pop("DBMS")
print(diccionario)
diccionario.clear()
print(diccionario)
del diccionario
print(diccionario)#da error porque se elimino el diccionario