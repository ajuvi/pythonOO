from abc import ABC,abstractmethod
import math

#classe abtracte
class Figura(ABC):

    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def pintar(self): pass

#implementació de la interfície pintar
class Rectangle(Figura):

    def __init__(self, x, y, amplada, alçada):
        super().__init__(x, y)
        #atributs d'objecte
        self.alçada = alçada
        self.amplada = amplada

    def pintar(self):
        print(self)

    def __str__(self):
        return f'Rectangle {self.amplada}x{self.alçada} ({self.x},{self.y})'        

#implementació de la interfície pintar
class Cercle(Figura):

    def __init__(self, x, y, radi):
        super().__init__(x, y)
        #atributs d'objecte
        self.radi = radi

    def pintar(self):
        print(self)

    def __str__(self):
        return f'Cercle r{self.radi} ({self.x},{self.y})'

#main
if __name__ == "__main__":
    figures = []
    #figures.append(Figura(0,0))
    figures.append(Rectangle(0,0,10,3))
    figures.append(Cercle(0,0,5))    
    figures.append(Rectangle(100,100,20,3))    
    figures.append(Cercle(100,50,10))       

    for f in figures:
        f.pintar()