from producto import Producto
from orden import Orden
producto1 = Producto("Uno",10.5)
producto2 = Producto("Dos",20.5)
producto3 = Producto("Tres",30.5)
productos=[producto1,producto2]
orden1=Orden(productos)
print(orden1)
print(orden1.calcularTotal())
print()
orden2 = Orden(productos)
orden2.agregarProducto(producto3)
print(orden2)
print(orden2.calcularTotal())