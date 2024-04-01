from abc import ABC, abstractmethod
import math

#declaració de interficie pintar
class IFigura(ABC):
    @abstractmethod
    def pintar(self): pass

#implementació de la interfície pintar
class Rectangle(IFigura):

    def __init__(self, x, y, amplada, alçada):
        #atributs d'objecte
        self.x = x
        self.y = y
        self.alçada = alçada
        self.amplada = amplada

    def pintar(self):
        print(self)

    def __str__(self):
        return f'Rectangle {self.amplada}x{self.alçada} ({self.x},{self.y})'        

#implementació de la interfície pintar
class Cercle(IFigura):

    def __init__(self, x, y, radi):
        #atributs d'objecte
        self.x = x
        self.y = y
        self.radi = radi

    def pintar(self):
        print(self)

    def __str__(self):
        return f'Cercle r{self.radi} ({self.x},{self.y})'

#main
if __name__ == "__main__":
    figures = []
    figures.append(Rectangle(0,0,10,3))
    figures.append(Cercle(0,0,5))    
    figures.append(Rectangle(100,100,20,3))    
    figures.append(Cercle(100,50,10))       

    for f in figures:
        f.pintar()