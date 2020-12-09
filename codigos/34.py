#codigo 34, ejemplo de uso del for con archivos
p = open("piensa.txt","r")

for x in p:#se itera sobre la instancia p
    print(x)#x es cada una de las lineas en p, estas se interpretan de manera separada

p.close()#esta funcion se encarga de cerrar el archivo
