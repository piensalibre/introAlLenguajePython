class Orden:
    contadorOrdenes = 0

    def __init__(self,productos):
        Orden.contadorOrdenes+=1
        self.__idOrden=Orden.contadorOrdenes
        self.__productos = productos

    def agregarProducto(self,producto):
        self.__productos.append(producto)

    def calcularTotal(self):
        total= 0
        for producto in self.__productos:
            total +=producto.getPrecio()
        return total

    def __str__(self):
        productosStr = ""
        for producto in self.__productos:
            productosStr+=producto.__str__() + "\n"
        return "Orden: "+str(self.__idOrden)+"\nProductos: \n"+productosStr