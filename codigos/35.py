#codigo 35, ejemplo de uso del modo append
p = open("piensa.txt","a")#se utiliza el modo append para agregar al archivo

p.write("\nAgregamos una nueva linea a nuestro archivo desde codigo en python")#el metodo write se usa para agregar una nueva linea al archivo, "\n" se usa para agregar un salto de linea

p.close()

o = open("piensa.txt","r")

print(o.read())
