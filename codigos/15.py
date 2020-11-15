#codigo 15, ejercicio con input
dato = input("Ingresa dato: ")#se ingresa un dato y se agrega a la variable dato

lista = ["hola","mundo","este","es","un","ejercicio"]#se declara una lista con valores ya establecidos

if lista.count(dato) > 0:#se cuenta el numero de veces que aparece el dato en la cadena, y si este es mayor a 0 se ejecuta la el if, sino el else
    print("El dato existe: ",dato)
else:
    print("El dato no existe: ",dato)
