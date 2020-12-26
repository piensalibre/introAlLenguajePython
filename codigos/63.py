#codigo 63, codigo que cuenta un caracter dentro de una palabra
palabra = "Hola"
cuenta = 0
for letra in palabra:
    if letra == 'o':
        cuenta = cuenta + 1
print(cuenta)