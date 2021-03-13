#codigo 142, repaso
nombres = ["Juan","Karla","Ricardo","Maria"]
print(nombres)
print(len(nombres))
print(nombres[0])
print(nombres[1])
print(nombres[2])
print(nombres[3])
print(nombres[-1])
print(nombres[-2])
print(nombres[-3])
print(nombres[-4])
print(nombres[0:2])
print(nombres[:3])
print(nombres[::-1])
print(nombres[1:])
nombres[2] = "Ivone"
print(nombres)
for nombre in nombres:
    print(nombre)
if "Karla" in nombres:
    print("Si esta la cadena")
else:
    print("El elemento buscado no esta en la lista")
nombres.append("Paco")
print(nombres)
nombres.insert(1,"Hugo")
print(nombres)
nombres.remove("Juan")
print(nombres)
print(nombres[0:2])
nombres.pop()
print(nombres)
del nombres[0]
print(nombres)
nombres.clear()
print(nombres)
del nombres
print(nombres)#la variable ya no existe, por eso imprime un error