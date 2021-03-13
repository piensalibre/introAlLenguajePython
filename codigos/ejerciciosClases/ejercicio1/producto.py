class Producto:

    contadorProducto = 0

    def __init__(self,nombre,precio):
        Producto.contadorProducto += 1
        self.__idProducto = Producto.contadorProducto
        self.__nombre=nombre
        self.__precio = precio
    
    def getPrecio(self):
        return self.__precio
    
    def __str__(self):
        return "Id producto: "+str(self.__idProducto)+"\nNombre: "+self.__nombre+"\nPrecio: "+str(self.__precio)
