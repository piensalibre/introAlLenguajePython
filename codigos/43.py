#codigo 34, funcion que indica cuantas vocales tiene una palabra
palabra = "Piensa"
vocales = 0
for c in palabra:
    x = c.lower()
    vocales += 1 if x == 'a' or x == 'e' or x == 'i' or x == 'o' or x == 'u' else 0

print(vocales)