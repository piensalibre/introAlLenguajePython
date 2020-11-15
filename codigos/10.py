#codigo 10, introduccion a valores booleanos y condicionales

verdadero = True#se asigna el valor booleano a la variable verdadero

falso = False#se asigna el valor booleano a la variable falso

print(verdadero,falso)

if 2 < 5:#con la condicional if se evalua la expresion que sigue, en este caso se evalua si 2 es menor que 5
    print("2 es menor que 5")#en caso que la expresion del if fuera evaluada como verdadera se ejecuta esta instruccion

if 2 == 2:#este if evalua si 2 es igual a 2, se usa doble igual "==" ya que si solo se usa 1 se estaria asignando el valor, y en este caso lo que se busca es comparar
    print("2 es igual a 2")

if 2 > 1:#con la condicional if se evalua la expresion que sigue, en este caso se evalua si 2 es mayor que 1
    print("2 es mayor que 1")#en caso que la expresion del if fuera evaluada como verdadera se ejecuta esta instruccion

if 2 != 3:#este if evalua si dos es distinto de 3, para esto se usa el operando '!' seguido del signo '='
    print("2 es distinto de 3")

if 2 != 2:#este if evalua si dos es distinto de 2, para esto se usa el operando '!' seguido del signo '='
    print("2 es distinto de 2")#esta instruccion no se ejecutara ya que la evaluacion del if da como resultado falso

if 3 <= 3:#este if evalua si 3 es menor o igual a 3
    print("3 es menor o igual a 3")

if 3 >= 3:#este if evalua si 3 es mayor o igual a 3
    print("3 es mayor o igual a 3")
