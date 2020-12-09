#codigo 18

primero = input("Ingresa un numero: ")

try:
    primero = int(primero)
except:
    primero = "Error"
    
if primero == "Error":
    print("Ingresaste un valor erroneo")
    exit()

segundo = input("Ingresa otro numero: ")

try:
    segundo = int(segundo)
except:
    segundo = "Error"
    
if segundo == "Error":
    print("Ingresaste un valor erroneo")
    exit()

simbolo = input("Igrese el simbolo de la operacion que desea: ")

if simbolo == '+':
    print("Suma: ",primero + segundo)
elif simbolo == '-':
    print("Resta: ",primero - segundo)
elif simbolo == '/':
    if segundo == 0:
        print("No es posible dividir entre 0")
        exit()
    print("Division: ",primero / segundo)
elif simbolo == '*':
    print("Multiplicacion: ",primero * segundo)
else:
    print("El simbolo indicado no es valido")