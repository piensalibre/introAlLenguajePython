#codigo 137, repaso
calificacion = int(input("Ingresa un valor entre 0 y 10: "))
if calificacion >= 9 and calificacion <= 10:
    print("A")
elif calificacion < 9 and calificacion >= 8:
    print("B")
elif calificacion >= 7 and calificacion <8:
    print("C")
elif calificacion >= 6 and calificacion <7:
    print("D")
elif calificacion >= 0 and calificacion <6:
    print("E")
else:
    print("Error al ingresar el valor")