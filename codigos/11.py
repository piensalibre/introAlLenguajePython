#codigo 11
if 2 > 5:
    print("2 es mayor a 5")
elif 2 < 5:#si el primer if da como resultado falso, esta instruccion permite realizar una segunda evaluacion
    print("2 es menor a 5")#esta linea se ejecutara ya que el primer if dio como resultado falso

if 2 == 5:
    print("2 es mayor a 5")
elif 2 > 5:
    print("2 es menor a 5")
else:#este else indica que el codigo que sigue se ejecutara siempre que el "if" o "elif" que lo preceden sean falsos
    print("2 no es igual ni mayor a 5")#esta linea se ejecutara ya que el "if" y el "elif" son falsos
