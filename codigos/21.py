#codigo 21, ejemplo de range en loops
for x in range(7):#este ciclo itera entre los valores de range, el cual esta definido del 0 hasta el 7
    print(x)

for x in range(1,10):#este ciclo itera en los valores de range los cuales estan definidos del 1 hasta el 10 ya que a range se le mando como primer argumento el valor de 1
    print(x)

for x in range(3,30,3):#este ciclo itera en los valores de range los cuales estan definidos del 3 hasta el 30 ya que a range se le mando como primer argumento el valor de 3 como segundo argumento el valor de 30, notese el tercer argumento el cual indica el incremento
    print(x)
else:#en los for loop la palabra reservada else se utiliza para ejecutar el codigo una vez terminada la iteracion del bucle
    print("Hemos terminado")