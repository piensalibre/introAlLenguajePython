#codigo 16, ejercicio mostrando diferencias entre el uso del operador + segun se use con cadenas o enteros y ejemplo de uso del try y del except validando datos
primero = input("Ingrese primer numero: ")
segundo = input("Ingrese segundo numero: ")

print(primero + segundo)#se imprimira la variable primero concatenada con la variable segundo, no se sumaron ya que al asignarse mediante la funcion input esta les asigna un valor tipo cadena y el operador '+' concatena las cadenas

try:#intenta ejecutar el codigo siguiente
    primerNumero = int(primero)#la funcion int() cambia el tipo de valor de la variable primero de cadena a entero

except:#en caso de no poder ejecutarse el codigo anterior se ejecutara el siguiente
    primero = "Error"

try:
    segundoNumero = int(segundo)

except:
    segundo = "Error"

if primero == "Error" or segundo == "Error":
    print("Ingresaste mal un dato, intenta de nuevo")
else:
    print(primerNumero + segundoNumero)#se imprimira la suma de primerNumero y segundoNumero ya que seran tratados como enteros si es que la validacion del try se ejecuto
