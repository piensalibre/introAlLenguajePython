#codigo 144, repaso
frutas = ("Naranja","Platano","Guayaba")
print(frutas)
print(len(frutas))
print(frutas[0])
print(frutas[-1])
print(frutas[0:2])
frutasLista = list(frutas)
print(frutas)
print(frutasLista)
frutasLista[1]="Platanito"
print(frutasLista)
frutas = tuple(frutasLista)
print(frutas)
print(frutasLista)
for fruta in frutas:
    print(fruta)
for fruta in frutas:
    print(fruta,end=" ")
print()
del frutas
print(frutas)#marca error debido a que se elimino la tupla