from abc import ABC,abstractclassmethod
class FiguraGeometrica(ABC):
    def __init__(self,ancho,alto):
        self.ancho=ancho
        self.alto=alto
    @abstractclassmethod
    def area(self):
        pass