#codigo 19, ejemplo de uso de loop
i = 0

while i < 5:#se inicia el ciclo while indicando que mientras i sea menor a 5 se ejecutara el siguiente codigo
    print(i)
    i += 1 #realiza un incremento de 1 a la variable i

i = 0

while i < 5:
    print(i)
    if i == 3:
        break#esta palabra reservada termina el ciclo
    i += 1 

i = 0

while i < 5:
    if i == 3:
        i +=1
        continue#esta palabra reservada salta el codigo que continua despues e regresa al ciclo while
    print(i)
    i += 1 